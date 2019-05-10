# -*- coding: utf-8 -*-
# @Author: leedagou
# @Date:   2019-05-01 16:10:13
# @Last Modified by:   leedagou
# @Last Modified time: 2019-05-05 21:49:50

import glob
writeFile = open('use_sql.txt', 'w')
writeFile.write('use gps_data;\n')
for filename in glob.glob(r'gpsdata\*.txt'):
    writeFile.write('load data local infile ' + '"' + filename.replace('\\', '/') + '"' +
                    ' into table db_gps  fields terminated by ",";\n')
writeFile.close()
