# -*- coding: UTF-8 -*-
# import windbgPy.pykd
# !load pykd.pyd
from  windbgPy import pykdPackage
from windbgPy import BpCondition

print("Hello")

# def getEprocessByName(name):
#     arc= pykdPackage.ptrSize()
#     list=pykdPackage.dbgCommand("!dml_proc")
#     list=list.split("\n")
#     list=list[1:len(list)-1]
#     for item in list:
#         if name in item:
#             if arc==4:
#                 ret = item[0:8]
#                 return "0x"+ret
#             else:
#                 ret = item[0:16]
#                 return "0x"+ret
#     return ""



def main():
    # print("_main_")
    # eax= pykdPackage.reg("eax")
    # print(eax)
    # eax=pykdPackage.getCurrentProcess()
    # # print(pykdPackage.Hex(eax))
    # # eax=pykdPackage.getModulesList()
    # # print (eax)
    # eax=pykdPackage.getCurrentEprocess()
    # # print(pykdPackage.Hex(eax))
    # print(eax)
    # ebx=getEprocessByName("explorer.exe ")
    # print(eax)
    # if  eax==ebx:
    #     print("ok")
    # # print(pykdPackage.addr64(int(eax)))

    #条件断点使用案例
    # NtOpenProcess=pykdPackage.getOffset("nt!NtOpenProcess")
    # bpCon=BpCondition.handleBpCondition(NtOpenProcess,"explorer.exe")
    # pykdPackage.go()
    ebx=pykdPackage.getMouleByName("nt")
    print(ebx.offset("PsLoadedModuleList"))
    print(ebx.type("_EPROCESS"))




if __name__ == '__main__':
    main()



