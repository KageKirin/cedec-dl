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
    todolist = qjph.load(args.list)
    pp.pprint(todolist)

    for k,v in todolist.items():
        print('downloading', v, 'as', k)
        p = args.output.joinpath(k)
        p.mkdir(parents=True, exist_ok=True)
        subprocess.run(["youtube-dl", "-c", "-w", "-o", k + ".mp4", v], cwd=p)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CEDEC Timeshift loader')
    parser.add_argument('-l', '--list', help='list containing the videos to load', type=Path)
    parser.add_argument('output', help='output dir', type=Path, default=Path('.'))
    args = parser.parse_args()
    pp.pprint(args)
    main(args)
