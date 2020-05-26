# -*- coding: UTF-8 -*-
#记录日志文件
import time
import pykdPackage

def logBinary(fineName,addrStart,size):
    '从addrStart拷贝size个字节，以二进制的形式'
    strtime = time.ctime()
    strtime = strtime.replace(':', ' ')
    fileNameTemp = '%s.bin' % strtime
    fileNameTemp=fineName+fileNameTemp
    dump = pykdPackage.loadBytes(int(addrStart, 16), int(size, 16))
    f = open(fileNameTemp, 'wb+')
    for a in dump:
        xx = int(a)
        b = chr(xx)
        f.write(b)
    f.close()

def logStr(fileName,content):
    '把content写入到fileName日志文件中'
    f = open(fileName, 'a')
    content=str(content)+'\n'
    f.write(content)
    f.close()
