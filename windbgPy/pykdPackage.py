# -*- coding: UTF-8 -*-
#重新封装的pykd
import pykd
#4表示32位架构，8表示64位架构
arc=pykd.ptrSize()

def Hex(arg):#-->str
    ret=hex(arg)
    return ret.replace('L','')


def go():
    pykd.go()

def dbgCommand(cmd):
    return pykd.dbgCommand(cmd)

def reg(register):
    return pykd.reg(register)

def loadBytes(addr,len):
    return pykd.loadBytes(addr,len)

def compareMemory(addr1,addr2,len):
    return pykd.compareMemory(addr1,addr2,len)

#0x7fffd18f0940L
#0:003> x kernel32!CreateFileW
#00007fff`d18f0940 KERNEL32!CreateFileW (<no parameter info>)
def getOffset(funName):
    return pykd.getOffset(funName)


#如果要查找基于符号的特殊地址处的函数，则应使用findSymbol
def findSymbol(addr):
    return pykd.findSymbol(addr)
#获取当前堆栈帧
def getFrame():
    return pykd.getFrame()
#
def getSystemVersion():
    return pykd.getSystemVersion()
#就是获取页面属性。
def getVaProtect(addr):
    return pykd.getVaProtect(addr)
#读取MSR寄存器
def rdmsr(value):
    return pykd.rdmsr(value)
#要在特定的MSR上写，可以使用pykd.wrmsr（Address，Value）。
def wrmsr(address,value):
    return pykd.wrmsr(address,value)
#Detach from all process and resume all their threads
def detachAllProcesses():
    return pykd.detachAllProcesses()
def detachProcess():
    return pykd.detachProcess()
def getLastException():
    return pykd.getLastException()
# 函数getCurrentProcess
# getCurrentProcess() -> int :
#     Return current offset
#     C++ signature :
#         unsigned __int64 getCurrentProcess()
def getCurrentProcess():
    return pykd.getCurrentProcess()

#断点
# 函数setBp
#
# setBp( (int)offset [, (object)callback]) -> breakpoint :
#     Set software breakpoint on executiont
#
#     C++ signature :
#         class pykd::Breakpoint * __ptr64 setBp(unsigned __int64 [,class boost::python::api::object {lvalue}])
#
# setBp( (int)offset, (int)size, (int)accsessType [, (object)callback]) -> breakpoint :
#     Set hardware breakpoint
#
#     C++ signature :
#         class pykd::Breakpoint * __ptr64 setBp(unsigned __int64,unsigned __int64,unsigned long [,class boost::python::api::object {lvalue}])
#
def setBp(addr,callback):
    return pykd.setBp(addr,callback)


#搜索内存
def searchMemory(startAddr,endAddr,target):
    return pykd.searchMemory(startAddr,endAddr,target)
#eb的等效项  是setByte
def setByte(addr,value):
    return  pykd.setByte(addr,value)
def setDWord(addr,valude):
    return pykd.setDWord(addr, value)
def setDouble(addr,valude):
    return pykd.setDouble(addr, value)
def setFloat(addr,valude):
    return pykd.setFloat(addr, value)
#修改eip
#可以使用setIP来更改当前的RIP或EIP，这在与打包程序和保护程序打败时非常有用
def setIP(eip):
    return pykd.setIP(eip)
def setSymbolPath(path):
    return pykd.setSymbolPath(path)
def step():
    return pykd.setp()
def stepout():
    return pykd.stepout()
def trace():
    return pykd.trace()
#反汇编
def disasm(addr):
    return pykd.disasm(addr)

#Extend address to 64 bits formats
def addr64(addr):
    return pykd.addr64(addr)
#Append current source path
def appendSrcPath(path):
    return pykd.appendSrcPath(path)
# Append current symbol path
def appendSymbolPath(path):
    return pykd.appendSymbolPath(path)
#Connect the debugger engine to a kernel target.
#    If connectOptions is not specified - attach to the local kernel
def attachKernel(path):
    return pykd.attachKernel(path)
def breakin():
    pykd.breakin()
def bugCheckData():
    return pykd.bugCheckData()
def callExt(intarg1,stragr2,strarg3):
    return pykd.callExt(intarg1,stragr2,strarg3)
def FunctionByAddr(args,kwds):
    return pykd.FunctionByAddr(args,kwds)
def FunctionByPtr(args,kwds):
    return pykd.FunctionByPtr(args,kwds)
def callFunctionRaw(args,kwds):
    return pykd.callFunctionRaw(args,kwds)
def currentTime():
    return pykd.currentTime()

# 函数getModulesList
#
# getModulesList() -> list :
#     Return list of modules for the current target
#
#     C++ signature :
#         class boost::python::list getModulesList()
#
def getModulesList():
    return pykd.getModulesList()


def ptrSize():
    return pykd.ptrSize()

# 函数getOffset
# getOffset( (str)arg1) -> int :
#     Return traget virtual address for specified symbol
#     C++ signature :
#         unsigned __int64 getOffset(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#根据字符串内容获得相应的地址
def getOffset(arg1):
    return pykd.getOffset(arg1)
def getCurrentProcess():
    return pykd.getCurrentProcess()
def getCurrentEprocess():
    arc= pykd.ptrSize()
    list=pykd.dbgCommand(".process")
    if arc == 4:
        ret = list[len(list)-1-8:len(list)-1]
        return "0x" + ret
    else:
        ret = list[len(list)-1-16:len(list)-1]
        return "0x" + ret
    return ""
#返回指针的长度，32位返回4,64位返回8，可用于判断操作系统是32位还是64位
def getEprocessByName(name):
    arc= pykd.ptrSize()
    list=pykd.dbgCommand("!dml_proc")
    list=list.split("\n")
    list=list[1:len(list)-1]
    for item in list:
        if name in item:
            if arc==4:
                ret = item[0:8]
                return "0x"+ret
            else:
                ret = item[0:16]
                return "0x"+ret
    return ""




#返回所有寄存器的值
def getAllRegisterValues():
    return pykd.dbgCommand("r")


# 方法targetSystem.isKernelDebugging
# isKernelDebugging( (targetSystem)arg1) -> bool :
#     Check if kernel dubugging is running
#     C++ signature :
#         bool isKernelDebugging(class kdlib::TargetSystem {lvalue})
def isKernelDebugging():
    return pykd.isKernelDebugging("r")

# name()
# image()
# pdb()
# begin()
# end()
# checksum()
# timestamp()
# 返回信息
# Module: ntdll
# Start: 77370000 End: 774ac000 Size: 13c000
# Image: ntdll.dll
# Symbols: D:\Windows Kits\10\Debuggers\x64\sym\ntdll.pdb\120028FA453F4CD5A6A404EC37396A582\ntdll.pdb
# Timestamp: 4ce7b96e (11/20/10 12:05:02)
# Check Sum: 1490d9
# nt = module("nt")
# print hex( nt.offset("PsLoadedModuleList") )
# print hex( nt.__getattr__("PsLoadedModuleList") )
# print hex( nt.PsLoadedModuleList )
# print(nt.type("_EPROCESS")) 显示结构体信息
# print nt.typedVar( "_LIST_ENTRY", nt.PsLoadedModuleList )
def getMouleByName(name):
    return pykd.module(name)

# kd> .formats 0x0000000000170678
# Evaluate expression:
#   Hex:     00000000`00170678
#   Decimal: 1508984
#   Octal:   0000000000000005603170
#   Binary:  00000000 00000000 00000000 00000000 00000000 00010111 00000110 01111000
#   Chars:   .......x
#   Time:    Sun Jan 18 19:09:44 1970
#   Float:   low 2.11454e-039 high 0
#   Double:  7.45537
#straddr可以是十六进制数字字符串0x0000000000170678或者0000000000170678
#也可以是寄存器，比如cr4
def formats(straddr):
    strTemp=".formats "+straddr
    return dbgCommand(strTemp)





