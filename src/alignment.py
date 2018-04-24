# -*- coding: utf-8 -*-

import os
import numpy as np
import cv2


class alignment(object):
    def __init__(self):
        pass

    def obtain_images(self, path):
        if os.path.isfile(path):
            self.files = [path]
        elif os.path.isdir(path):
            self.files =  [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]
            basedir = os.path.dirname(path)
            for i in range(len(self.files)):
                self.files[i] = os.path.join(basedir, self.files[i])
        else: self.files = []
        return len(self.files)

    def get_center(self):
        pass

    def process(self, move = True):
        for img_file in self.files:
            try:
                new_file = os.path.join(os.path.dirname(img_file), 'out', os.path.basename(img_file))
                #print(img_file)
                img = cv2.imread(img_file)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                gray = cv2.GaussianBlur(gray, (5, 5), 0)
                thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)[1]
                im2, cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
                rows, cols = gray.shape

                for i, cnt in enumerate(cnts):
                    area = cv2.contourArea(cnt)
                    if area > 5000:
                        epsilon = 10*cv2.arcLength(cnt,True)
                        approx = cv2.approxPolyDP(cnt,epsilon,True)
                        M = cv2.moments(cnt)

                        cx = int(M['m10']/M['m00'])
                        cy = int(M['m01']/M['m00'])

                        ellipse = cv2.fitEllipse(cnt)
                        #cv2.ellipse(img, ellipse, (10,10,225),1)       # vykresluje vypocitanou elipsu
                        #cv2.circle(img, (cx, cy), 5, (255, 10, 10), 3) # vykresluje stred slunce

                #print(cols/2, rows/2)
                #print(cx, cy)
                M = np.float32([[1,0,cols/2-cx],[0,1,rows/2-cy]])
                dst = cv2.warpAffine(img,M,(cols,rows))
                cv2.imwrite(new_file, dst)
                print(new_file)
            except Exception as e:
                print("Err>>", img_file)
                print(e)

if __name__ == '__main__':
    SA = alignment()
    SA.obtain_images(def_path)
    SA.files
    SA.process()
