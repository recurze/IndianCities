#!/usr/bin/env python3

import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

area_prefix_url = "https://villageinfo.in/"
latlong_prefix_url = "https://www.latlong.net/search.php?keyword="
wiki_prefix_url = "https://en.wikipedia.org/wiki/"

def getlatlong(cityname):
    print("Searching: " + cityname, file = sys.stderr)
    browser.get(latlong_prefix_url+cityname)
    lat, lon = '0', '0'
    try:
        table = browser.find_element(By.TAG_NAME, 'table')
        rows = table.find_elements(By.TAG_NAME, "tr")
        if len(rows) == 2:
            lat = rows[1].find_elements(By.TAG_NAME, "td")[1].text
            lon = rows[1].find_elements(By.TAG_NAME, "td")[2].text
    except:
        lat, lon = '0', '0'
    return lat, lon

def add_latlong(ifname, ofname):
    with open(ifname, 'r') as inf:
        with open(ofname, 'w') as outf:
            for line in inf:
                line = line.strip().split(',')
                cityname, statename = line[2], line[0]
                lat, lon = getlatlong(cityname + ', ' + statename)
                if lat == '0':
                    print("Missing:", cityname, statename, file = sys.stderr)
                print(','.join(line + [lat, lon]), file = outf)

def todeci(coord):
    if '°' not in coord: return coord
    a = coord.split('°')
    b = a[1].split('′')
    return str(int(a[0]) + int(b[0])/60.0)

def wiki_get_latlong(cityname):
    print("Searching: " + cityname, file = sys.stderr)
    browser.get(wiki_prefix_url+cityname)
    if browser.current_url != wiki_prefix_url+cityname:
        return "0", "0"
    try:
        lat = browser.find_element(By.XPATH, ".//span[@class='latitude']").get_attribute('innerText')
        lon = browser.find_element(By.XPATH, ".//span[@class='longitude']").get_attribute('innerText')
        return todeci(lat), todeci(lon)
    except:
        return "0", "0"


def wiki_add_latlong(ifname, ofname):
    with open(ifname, 'r') as inf:
        with open(ofname, 'w') as outf:
            for line in inf:
                line = line.strip().split(',')
                if line[-1] == "0":
                    cityname = line[2]
                    lat, lon = wiki_get_latlong(cityname)
                    if lat == '0':
                        statename = line[0]
                        print("Missing:", cityname, statename, file = sys.stderr)
                    print(','.join(line[:-2] + [lat, lon]), file = outf)
                else:
                    print(','.join(line), file = outf)

def getarea(cityname, districtname, statename):
    print("Searching for area of", cityname, districtname, statename)
    cityname = cityname.replace(' ', '-')
    statename = statename.replace(' ', '-')
    districtname = districtname.replace(' ', '-')
    extension = statename + '/' + districtname + '/' + cityname + '.html'
    browser.get(area_prefix_url + extension)
    area = '0'
    try:
        tables = browser.find_elements(By.TAG_NAME, "table")
        for table in tables:
            rows = table.find_elements(By.TAG_NAME, "tr")
            if len(rows) == 6:
                if 'area' in rows[4].find_elements(By.TAG_NAME, "td")[0].text.lower():
                    area = rows[4].find_elements(By.TAG_NAME, "td")[1].text
                    area = area[:area.find('k')].replace(',', '')
    except:
        area = '0'
    return area

def wiki_get_area(cityname, districtname, statename):
    print("Searching: " + cityname, file = sys.stderr)
    cityname = cityname.replace(' ', '_')
    browser.get(wiki_prefix_url+cityname)
    if browser.current_url != wiki_prefix_url+cityname:
        return "0"
    try:
        html_source = browser.page_source
        if "&nbsp;km<sup>2</sup>" in html_source:
            print("Yay")
            while 1:
                j = html_source.find("&nbsp;km<sup>2</sup>")
                if j == -1: break
                i = j - 1
                while html_source[i].isdigit() or html_source[i] == '.': i -= 1
                if html_source[i] == '>':
                    print("Finally")
                    return html_source[i + 1: j]
                html_source = html_source[j + 1:]
        return "0"
    except:
        return "0"

def add_area(ifname, ofname):
    with open(ifname, 'r') as inf:
        with open(ofname, 'w') as outf:
            for line in inf:
                line = line.strip().split(',')
                if line[-1] == '0':
                    cityname, districtname, statename = line[2], line[1], line[0]
                    area = wiki_get_area(cityname, districtname, statename)
                else: area = line[-1]
                print(','.join(line[:-1] + [area]), file = outf)
                continue
                cityname, districtname, statename = line[2], line[1], line[0]
                area = getarea(cityname, districtname, statename)
                if area == '0':
                    print("Missing:", cityname, districtname, statename, file = sys.stderr)
                print(','.join(line + [area]), file = outf)

if __name__ == "__main__":
    opts = Options()
    opts.headless = True
    browser = webdriver.Firefox(options = opts)
    add_area(*sys.argv[1:])
    browser.close()
