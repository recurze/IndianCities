#!/usr/bin/env python3

import sys

def strip(ifname, ofname):
    with open(ofname, 'w') as outf:
        with open(ifname, 'r') as inf:
            for line in inf:
                line = line.split(',')
                a = line[0:4] + [line[7],line[10]]
                print(','.join(a), file=outf)

def filter(ifname, ofname):
    with open(ofname, 'w') as outf:
        with open(ifname, 'r') as inf:
            for line in inf:
                if int(line.strip().split(',')[-1]) > 100000:
                    print(line.strip(), file=outf)

def consolidate(ifname, ofname):
    with open(ofname, 'w') as outf:
        d = {}
        with open(ifname, 'r') as inf:
            for line in inf:
                name = line.split(',')[-2]
                if "Part" in name and "OG" not in name:
                    print(line.strip(), file=outf)
                elif int(line.split(',')[3]) not in d:
                    print(line.strip(), file=outf)
                    d[int(line.split(',')[3])] = 1

def codes(ifname, sname, dname, ofname):
    s = {}
    with open(sname, 'r') as f:
        for line in f:
            line = line.split(',')
            s[line[0]] = line[1]
    d = {}
    with open(dname, 'r') as f:
        for line in f:
            line = line.split(',')
            d[line[1]] = line[2]
    with open(ofname, 'w') as outf:
        with open(ifname, 'r') as inf:
            for line in inf:
                line = line.strip().split(',')
                a = [s[line[0]], d[line[1]]] + line[2:]
                print(','.join(a), file=outf)

if __name__ == "__main__":
    codes(*sys.argv[1:])
