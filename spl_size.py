# -*- coding: utf-8 -*-
# @Author: leedagou
# @Date:   2019-04-30 16:21:18
# @Last Modified by:   leedagou
# @Last Modified time: 2019-05-07 23:27:32

# encoding=utf-8

import os
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from datetime import datetime


def splitfile(filepath, partialsize=1024 * 1024 * 100):
    print("开始时间")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    filedir, name = os.path.split(filepath)
    print(filedir, name)
    name, ext = os.path.splitext(name)
    print(name, ext)
    filedir = os.path.join(filedir, name)
    if not os.path.exists(filedir):
        os.mkdir(filedir)
    partno = 0
    stream = open(filepath, 'rb')
    while True:
        partfilename = os.path.join(filedir, name + '_' + str(partno) + ext)
        # print('write start %s' % partfilename)
        part_stream = open(partfilename, 'wb')
        read_count = 0
        read_size = 1024 * 512 * 16
        read_count_once = 0
        while read_count < partialsize:
            read_content = stream.read(read_size)
            read_count_once = len(read_content)
            if read_count_once > 0:
                part_stream.write(read_content)
            else:
                break
            read_count += read_count_once

        line = stream.readline()
        part_stream.write(line)
        part_stream.close()
        if(read_count_once < read_size):
            break
        partno += 1
    print("结束时间")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    splitfile(r'')
