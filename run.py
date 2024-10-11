import json
import os
import argparse
import sys
import subprocess
import ghlinguist as ghl
import requests


def parse_arguments():
    parser = argparse.ArgumentParser())
    parser.add_argument('path', type=str, help='Path name')
    return parser.parse_args()

def main(full_path):
    # linguist_version = subprocess.run(["github-linguist", "--version"], capture_output=True).stdout.decode('utf-8').strip()
    #Use ghlinguist to run linguist on the repo (need to supply the full path not just the name)
    return ghl.linguist(full_path, True)


if __name__ == "__main__":
    args = parse_arguments()
    print(args.path)
    main(args.path)
    


