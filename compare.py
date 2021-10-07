#!/usr/bin/python3
# compare.py
import argparse
from correlation import correlate

def initialize():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i ", "--source-file", help="source file")
    parser.add_argument("-o ", "--target-file", help="target file")
    args = parser.parse_args()
  
    SOURCE_FILE = args.source_file if args.source_file else None
    TARGET_FILE = args.target_file if args.target_file else None
    if not SOURCE_FILE or not TARGET_FILE:
      raise Exception("Source or Target files not specified.")
    return SOURCE_FILE, TARGET_FILE
  
if __name__ == "__main__":
    SOURCE_FILE, TARGET_FILE = initialize()
    correlate(SOURCE_FILE, TARGET_FILE)
