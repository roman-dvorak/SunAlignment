#!/usr/bin/python
# -*- coding: utf-8 -*-

from src import alignment
import argparse

def main():
    parser = argparse.ArgumentParser(description='Simple image alignment tool...')
    parser.add_argument('path', action="store", type=str,  help = "Path to image or path to directory with images")

    SA = alignment.alignment()
    SA.obtain_images(parser.parse_args().path)
    SA.process()


if __name__ == '__main__':
    main()
