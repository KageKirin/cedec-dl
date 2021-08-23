#!/usr/bin/env python3

import os, sys, re, codecs, site, pprint, subprocess
site.addsitedir(os.path.dirname(__file__))
import argparse, keyring, toml
from pathlib import Path
import colorama
colorama.init()
import qjph.qjph as qjph
pp = pprint.PrettyPrinter()

def main(args):
    print('downloading', args.url, 'as', args.output)
    subprocess.run(["youtube-dl", "--list-formats", args.url])
    fmt = input("Select format (number only)")
    while(True):
        subprocess.run(["youtube-dl", "--continue", "--no-overwrites", "--restrict-filenames", "-f", fmt, args.url], cwd=args.output)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CEDEC Timeshift loader')
    parser.add_argument('-u', '--url', help='url to load')
    parser.add_argument('output', help='output dir', type=Path, default=Path('.'))
    args = parser.parse_args()
    pp.pprint(args)
    main(args)
