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

    proc = []
    for k,v in todolist.items():
        print('downloading', v, 'as', k)
        p = args.output.joinpath(k)
        p.mkdir(parents=True, exist_ok=True)
        pp = subprocess.Popen(["youtube-dl", "--continue", "--no-overwrites", "--restrict-filenames", "-o", k + ".mp4", v], cwd=p, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc.append(pp)

    while True:
        for p in proc:
            rc = p.poll()
            if rc:
                #restart
                p = subprocess.Popen(p.args, cwd=p.cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                #print
                print(proc.index(p), "(out):", p.stdout)
                print(proc.index(p), "(err):", p.stderr)




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CEDEC Livestream loader')
    parser.add_argument('-l', '--list', help='list containing the videos to load', type=Path)
    parser.add_argument('output', help='output dir', type=Path, default=Path('.'))
    args = parser.parse_args()
    pp.pprint(args)
    main(args)
