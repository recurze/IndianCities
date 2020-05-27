#!/usr/bin/env python3

import pandas

IFNAME = 'final_cities.csv'

def cities(ifname = IFNAME):
    return pandas.read_csv(ifname)

def printall(ifname = IFNAME):
    with open(ifname) as f:
        for line in f:
            line = line.strip().split(',')
            if line[0] == 'State': continue
            print("State         :  ", line[0])
            print("District      :  ", line[1])
            print("City          :  ", line[2])
            print("Population    :  ", line[3])
            print("Latitude      :  ", line[4])
            print("Latitude      :  ", line[5])
            print("Area          :  ", line[6])
            print()

if __name__ == "__main__":
    printall()
