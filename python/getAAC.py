#!/usr/bin/python
# get aac file from flvs
import os
import glob
import xml.etree.ElementTree as ET

flv_files = glob.glob('./*.flv')
# print flv_files
# print ret
for flv in flv_files:
    # print flv
    cmd = 'mediainfo --OUTPUT=XML ' + flv
    ret = os.popen(cmd).read()
    root = ET.fromstring(ret)
    general_info = root[0][0]
    name = flv
    track_name = general_info.find('Track_name')
    if track_name != None:
        name = track_name.text
    # print name
    cmd = ' ffmpeg -i ' + flv + ' -vn -acodec copy \"' + name + '.aac\"'
    print cmd
    os.system(cmd)
