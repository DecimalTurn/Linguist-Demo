import json
import os
import argparse
import sys
import subprocess
import ghlinguist as ghl
import requests


def parse_arguments():
    parser = argparse.ArgumentParser(description="Get path information")
    parser.add_argument('path', type=str, help='Path name')
    return parser.parse_args()

def main(full_path):
    # linguist_version = subprocess.run(["github-linguist", "--version"], capture_output=True).stdout.decode('utf-8').strip()
    #Use ghlinguist to run linguist on the repo (need to supply the full path not just the name)
    lang = ghl.linguist(full_path, True)
    
    if lang is None:
        print(f"Failed to determine the language of repo {slug}")
        problem_encountered = True
        return
        
    print(f"Output: {lang}")


if __name__ == "__main__":
    print("Starting")
    args = parse_arguments()
    print(args.path)
    main(args.path)
    


