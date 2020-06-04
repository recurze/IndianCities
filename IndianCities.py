#!/usr/bin/env python3

import pandas

IFNAME_STATES = 'final_states.csv'
IFNAME_DISTRICTS = 'final_districts.csv'
IFNAME_CITIES = 'final_cities.csv'
IFNAME_ALL = 'india_places.csv'

def states(ifname = IFNAME_STATES):
    return pandas.read_csv(ifname)

def districts(ifname = IFNAME_DISTRICTS):
    return pandas.read_csv(ifname)

def cities(ifname = IFNAME_CITIES):
    return pandas.read_csv(ifname)

def all(ifname = IFNAME_ALL):
    return pandas.read_csv(ifname)

def printstates(ifname = IFNAME_STATES):
    with open(ifname) as f:
        for line in f:
            line = line.strip().split(',')
            if line[0] == 'State': continue
            print("State                :  ", line[0])
            print("Number of Districts  :  ", line[1])
            print("Population           :  ", line[2])
            print("Area                 :  ", line[3])
            print()

def printdistricts(ifname = IFNAME_DISTRICTS):
    with open(ifname) as f:
        for line in f:
            line = line.strip().split(',')
            if line[0] == 'State': continue
            print("State         :  ", line[0])
            print("District      :  ", line[1])
            print("Population    :  ", line[2])
            print("Area          :  ", line[3])
            print()

def printcities(ifname = IFNAME_CITIES):
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

def printall():
    printstates()
    printdistricts()
    printcities()

if __name__ == "__main__":
    printall()
