# -*- coding: UTF-8 -*-
import pykd
import pykdPackage


#enter_call_back返回false表示处理了，true表示没有处理
#构造函数传递的是要hook地址，16进制数或者10进制数
#targetProcessName需要对哪个进程进行关照
class handleBpCondition(pykd.eventHandler):
    targetEprocess=""
    def __init__(self,addr,targetProcessName):
        self.bp_init = pykdPackage.setBp(addr, self.enter_call_back)
        self.bp_end = None
        self.targetEprocess = pykdPackage.getEprocessByName(targetProcessName)
        print("handleBpCondition ok")
        print(addr)
    def enter_call_back(self):
        CurrentEprocess = pykdPackage.getCurrentEprocess()
        print(CurrentEprocess)
        if CurrentEprocess == self.targetEprocess:
            print("ok")
            return True
        return False

    def return_call_back(self, bp):
        # returns a BOOLEAN which is a byte under the hood
        ret_val = hex(pykd.reg("al"))
        log.write(self.out + ret_val + "\n")
        return False
# 从startAddr跟踪到endAddr，限定函数跳转在constraitStartAddr到constraitEndaddr
class trace(pykd.eventHandler):
    startAddr=0
    endAddr=0
    def __init__(self,startAddr,endAddr,constraitStartAddr,constraitEndaddr):
        pass