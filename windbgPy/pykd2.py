import pykd
# # 函数addSyntheticModule
# # addSyntheticModule( (int)base, (int)size, (str)name [, (str)path]) -> None :
# #     The addSyntheticModule function adds a synthetic module to the module list the debugger maintains for the current process
# #     C++ signature :
# #         void addSyntheticModule(unsigned __int64,unsigned long,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > [,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >])
def addSyntheticModule(base,size,name,*args):
    return pykd.addSyntheticModule(base,size,name,args)
#
# # addSyntheticSymbol( (int)arg1, (int)arg2, (str)arg3) -> syntheticSymbol :
# #     The addSyntheticSymbol function adds a synthetic symbol to a module in the current process
# #     Note: reloading the symbols for the module deletes all synthetic symbols associated with that module.
# #
# #     C++ signature :
# #         struct kdlib::SyntheticSymbol addSyntheticSymbol(unsigned __int64,unsigned long,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
def addSyntheticSymbol(arg1,arg2,arg3):
    return  addSyntheticSymbol(arg1,arg2,arg3)
#
#
#
#
# # 功能addr64
# # addr64( (int)arg1) -> int :
# #     Extend address to 64 bits formats
# #     C++ signature :
# #         unsigned __int64 addr64(unsigned __int64)
def addr64(arg1):
    return pykd.addr64(arg1)
#
#
# # 函数appendSrcPath
# # appendSrcPath( (str)arg1) -> None :
# #     Append current source path
# #     C++ signature :
# #         void appendSrcPath(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
def appendSrcPath(arg1):
    return pykd.appendSrcPath(arg1)
#
#
# # 函数appendSymbolPath
# # appendSymbolPath( (str)arg1) -> None :
# #     Append current symbol path
# #     C++ signature :
# #         void appendSymbolPath(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
def appendSymbolPath(arg1):
    return pykd.appendSymbolPath(arg1)
#
#
#
# # 功能attachKernel
# # attachKernel([  (str)connectOptions]) -> None :
# #     Connect the debugger engine to a kernel target.
# #     If connectOptions is not specified - attach to the local kernel
# #     C++ signature :
# #         void attachKernel([ class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >])
def attachKernel(*arg1):
    return pykd.appendSymbolPath(*arg1)
#
#
# # 功能attachProcess
# # attachProcess( (int)pid [, (int)debugOptions]) -> int :
# #     Attach debugger to a exsisting process
# #
# #     C++ signature :
# #         unsigned long attachProcess(unsigned long [,unsigned long])
def attachProcess(pid,*arg1):
    return pykd.attachProcess(pid,*arg1)
#
#
# # 功能破解
# # breakin() -> None :
# #     Break into debugger
# #
# #     C++ signature :
#         void breakin()
def breakin():
    return pykd.breakin()
#
#
# # 函数bugCheckData
# # bugCheckData() -> tuple :
# #     Function reads the kernel bug check code and related parameters
# #     And return tuple: (code, arg1, arg2, arg3, arg4)
# #     C++ signature :
# #         class boost::python::tuple bugCheckData()
def bugCheckData():
    return pykd.breakin()
#
#
# # 函数callExt
# # callExt( (int)arg1, (str)arg2, (str)arg3) -> str :
# #     Call a WinDBG extension's routine. Parameters: handle returned by loadExt; string command line
# #
# #     C++ signature :
# #         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > callExt(unsigned __int64,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
def callExt(arg1,arg2,arg3):
    return pykd.callExt(arg1,arg2,arg3)
#
#
# # 函数调用FunctionByAddr
# # object callFunctionByAddr(tuple args, dict kwds) :
# #
# #     C++ signature :
# #         object callFunctionByAddr(tuple args, dict kwds)
def callFunctionByAddr(args,kwds):
    return pykd.callFunctionByAddr(args,kwds)
#
#
# # 函数调用FunctionByPtr
# #
# # object callFunctionByPtr(tuple args, dict kwds) :
# #
# #     C++ signature :
# #         object callFunctionByPtr(tuple args, dict kwds)
def callFunctionByPtr(args,kwds):
    return pykd.callFunctionByPtr(args,kwds)
#
# # 函数调用FunctionRaw
# #
# # object callFunctionRaw(tuple args, dict kwds) :
# #
# #     C++ signature :
# #         object callFunctionRaw(tuple args, dict kwds)
def callFunctionRaw(args,kwds):
    return pykd.callFunctionRaw(args,kwds)
#
# # 函数changeDebugOptions
# #
# # changeDebugOptions( (int)arg1, (int)arg2) -> None :
# #     Change debug options
# #
# #     C++ signature :
# #         void changeDebugOptions(unsigned long {lvalue},unsigned long {lvalue})
def changeDebugOptions(arg1,arg2):
    return pykd.changeDebugOptions(arg1,arg2)
#
#
# # 函数closeDump
# #
# # closeDump([  (int)id]) -> None :
# #     Close crash dump
# #
# #     C++ signature :
# #         void closeDump([ unsigned long])
def closeDump(*arg1):
    return pykd.closeDump(*arg1)
#
#
# # 功能compareMemory
# # compareMemory( (int)offset1, (int)offset2, (int)length [, (bool)phyAddr]) -> bool :
# #     Compare two memory buffers by virtual or physical addresses
# #
# #     C++ signature :
# #         bool compareMemory(unsigned __int64,unsigned __int64,unsigned __int64 [,bool])
def compareMemory(startAddr,endaddr,len):
    return pykd.compareMemory(startAddr,endaddr,len)
#
#
# 函数包含记录
#
# containingRecord( (int)arg1, (str)arg2, (str)arg3) -> typedVar :
#     Return instance of the typedVar class. It's value are loaded from the target memory.The start address is calculated by the same method as the standard macro CONTAINING_RECORD does
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> containingRecord(unsigned __int64,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
# containingRecord( (int)arg1, (typeInfo)arg2, (str)arg3) -> typedVar :
#     Return instance of the typedVar class. It's value are loaded from the target memory.The start address is calculated by the same method as the standard macro CONTAINING_RECORD does
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> containingRecord(unsigned __int64,class boost::shared_ptr<class kdlib::TypeInfo> {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 函数createStruct
#
# createStruct( (str)name [, (int)align]) -> typeInfo :
#     Create custom struct
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> createStruct(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > [,unsigned __int64])
#
#
# 函数createUnion
#
# createUnion( (str)name [, (int)align]) -> typeInfo :
#     Create custom union
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> createUnion(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > [,unsigned __int64])
#
#
# 函数currentTime
#
# currentTime() -> int :
#     Return the number of seconds since the beginning of 1970
#
#     C++ signature :
#         unsigned long currentTime()
def currentTime():
    return pykd.currentTime()
#
#
# 功能dbgCommand
#
# dbgCommand( (str)command [, (bool)suppressOutput]) -> object :
#     Run a debugger's command and return it's result as a string
#
#     C++ signature :
#         class boost::python::api::object dbgCommand(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > [,bool])
#
def dbgCommand(command):
    return pykd.dbgCommand(command)

#
# 功能定义功能
#
# defineFunction( (typeInfo)returnType [, (callingConvention)callconv]) -> typeInfo :
#     Define custom function prototype
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> defineFunction(class boost::shared_ptr<class kdlib::TypeInfo> [,enum kdlib::CallingConventionType])
#
#
# 函数取消初始化
#
# deinitialize() -> None :
#     Deintialize debug engine, only for console mode
#
#     C++ signature :
#         void deinitialize()
#
#
# 函数detachAllProcesses
#
# detachAllProcesses() -> None :
#     Detach from all process and resume all their threads
#
#     C++ signature :
#         void detachAllProcesses()
#
def detachAllProcesses():
    return pykd.detachAllProcesses()
#
# 功能分离过程
#
# detachProcess([  (int)id]) -> None :
#     Stop process debugging
#
#     C++ signature :
#         void detachProcess([ unsigned long])
#
def detachProcess(pid):
    return pykd.detachProcess(pid)
#
# 函数dinput
#
# dinput( (str)arg1) -> None :
#     Provide input for debugger
#
#     C++ signature :
#         void dinput(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
def dinput(arg1):
    return pykd.dinput(arg1)
#
# 功能dprint
#
# dprint( (str)str [, (bool)dml]) -> None :
#     Print out string. If dml = True string is printed with dml highlighting ( only for windbg )
#
#     C++ signature :
#         void dprint(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > [,bool])
#
#
# 功能dprintln
#
# dprintln( (str)str [, (bool)dml]) -> None :
#     Print out string and insert end of line symbol. If dml = True string is printed with dml highlighting ( only for windbg )
#
#     C++ signature :
#         void dprintln(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > [,bool])
#
#
# 函数enumTagged
#
# enumTagged() -> list :
#     Return the list of secondary callback data IDs (as a strings)
#
#     C++ signature :
#         class boost::python::list enumTagged()
#
#
# 函数evalExpr
#
# evalExpr( (str)expression [, (object)scope [, (typeInfoProvider)typeProvider]]) -> typedVar :
#     Evaluate C++ expression with typed information
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> evalExpr(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,class boost::python::api::object {lvalue} [,class boost::shared_ptr<class kdlib::TypeInfoProvider> {lvalue}]])
#
#
# 函数expr
#
# expr( (str)expression [, (bool)cplusplus]) -> object :
#     Evaluate windbg expression
#
#     C++ signature :
#         class boost::python::api::object expr(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > [,bool])
#
#
# 函数findMemoryRegion
#
# findMemoryRegion( (int)arg1) -> tuple :
#     Return address of begining valid memory region nearest to offset
#
#     C++ signature :
#         class boost::python::tuple findMemoryRegion(unsigned __int64)
#
#
def findMemoryRegion(arg1):
    return pykd.findMemoryRegion(arg1)

# 函数findSymbol
#
# findSymbol( (int)offset [, (bool)showDisplacement]) -> str :
#     Find symbol by the target virtual memory offset
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > findSymbol(unsigned __int64 [,bool])
#
def findSymbol(addr):
    return pykd.findSymbol(addr)
#
# 函数findSymbolAndDisp
#
# findSymbolAndDisp( (int)arg1) -> tuple :
#     Return tuple (module_name, symbol_name, displacement) by virtual address
#
#     C++ signature :
#         class boost::python::tuple findSymbolAndDisp(unsigned __int64)
#
def findSymbolAndDisp(addr):
    return pykd.findSymbolAndDisp(addr)
#
# 函数getBp
#
# getBp( (int)arg1) -> breakpoint :
#     Return breakpoint object by index
#
#     C++ signature :
#         class pykd::Breakpoint * __ptr64 getBp(unsigned long)
#
#
def getBp(arg1):
    return pykd.getBp(arg1)
# 函数getCPUMode
#
# getCPUMode() -> CPUType :
#     Return current processor mode: CPUType
#
#     C++ signature :
#         enum kdlib::CPUType getCPUMode()
#
#
def getCPUMode():
    return pykd.getCPUMode()
# 函数getCPUType
#
# getCPUType() -> CPUType :
#     Return type of physical processor: CPUType
#
#     C++ signature :
#         enum kdlib::CPUType getCPUType()
#
#
# 函数getCurrentProcess
#
# getCurrentProcess() -> int :
#     Return current offset
#
#     C++ signature :
#         unsigned __int64 getCurrentProcess()
#
def getCurrentProcess():
    return pykd.getCurrentProcess()
#
# 函数getCurrentProcessId
#
# getCurrentProcessId() -> int :
#     Return current process ID
#
#     C++ signature :
#         unsigned long getCurrentProcessId()
#
def getCurrentProcessId():
    return pykd.getCurrentProcessId()
#
# 函数getCurrentThread
#
# getCurrentThread() -> int :
#     Return current thread offset
#
#     C++ signature :
#         unsigned __int64 getCurrentThread()
#
def getCurrentThread():
    return pykd.getCurrentThread()
#
# 函数getCurrentThreadId
#
# getCurrentThreadId() -> int :
#     Return current thread ID
#
#     C++ signature :
#         unsigned long getCurrentThreadId()
#
def getCurrentThreadId():
    return pykd.getCurrentThreadId()
#
# 函数getDebugOptions
#
# getDebugOptions() -> int :
#     Return debug options
#
#     C++ signature :
#         unsigned long getDebugOptions()
def getDebugOptions():
    return pykd.getDebugOptions()
#
#
# 函数getExecutionStatus
#
# getExecutionStatus() -> executionStatus :
#     Return current execution status
#
#     C++ signature :
#         enum kdlib::ExecutionStatus getExecutionStatus()
#
def getExecutionStatus():
    return pykd.getExecutionStatus()
#
# 函数getExtensionSearchPath
#
# getExtensionSearchPath() -> str :
#     Return the extension DLL search path
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > getExtensionSearchPath()
#
def getExtensionSearchPath():
    return pykd.getExtensionSearchPath()
#
# 函数getFP
#
# getFP() -> int :
#     Return frame pointer
#
#     C++ signature :
#         unsigned __int64 getFP()
#
def getFP():
    return pykd.getFP()
#
# 函数getFrame
#
# getFrame() -> stackFrame :
#     Return a current stack frame
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::StackFrame> getFrame()
#
def getFrame():
    return pykd.getFrame()
#
# 函数getFrameNumber
#
# getFrameNumber() -> int :
#     Return current frame number
#
#     C++ signature :
#         unsigned long getFrameNumber()
#
def getFrameNumber():
    return pykd.getFrameNumber()
#
# 函数getHostProcessPath
#
# getHostProcessPath() -> str :
#     Return image path of the process running python interpreter with a pykd
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > getHostProcessPath()
#
def getHostProcessPath():
    return pykd.getHostProcessPath()
#
# 功能getIP
#
# getIP() -> int :
#     Return instruction pointer
#
#     C++ signature :
#         unsigned __int64 getIP()
#
def getIP():
    return pykd.getIP()
#
# 函数getImplicitProcess
#
# getImplicitProcess() -> int :
#     Return implicit process
#
#     C++ signature :
#         unsigned __int64 getImplicitProcess()
#
def getImplicitProcess():
    return pykd.getImplicitProcess()
#
# 函数getImplicitThread
#
# getImplicitThread() -> int :
#     Return implicit thread
#
#     C++ signature :
#         unsigned __int64 getImplicitThread()
def getImplicitThread():
    return pykd.getImplicitThread()
#
#
# 函数getLastEvent
#
# getLastEvent() -> debugEvent :
#     Get last debug event information
#
#     C++ signature :
#         struct pykd::DebugEvent getLastEvent()
def getLastEvent():
    return pykd.getLastEvent()
#
#
# 函数getLastException
#
# getLastException() -> exceptionInfo :
#     Get last exception  information
#
#     C++ signature :
#         struct kdlib::ExceptionInfo getLastException()
#
def getLastException():
    return pykd.getLastException()
#
# 函数getLocal
#
# getLocal( (str)arg1) -> typedVar :
#     Get the fucntion's local variable by name
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> getLocal(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
def getLocal(arg1):
    return pykd.getLocal(arg1)
#
# 函数getLocalProcesses
#
# getLocalProcesses() -> list :
#     Return list of runnng processes on the host system
#
#     C++ signature :
#         class boost::python::list getLocalProcesses()
#
def getLocalProcesses():
    return pykd.getLocalProcesses()
#
# 函数getLocals
#
# getLocals() -> list :
#     Get list of local variables
#
#     C++ signature :
#         class boost::python::list getLocals()
def getLocals():
    return pykd.getLocals()
#
#
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
#
# 函数getNumberBreakpoints
#
# getNumberBreakpoints() -> int :
#     Return number of breakpoints in the current process
#
#     C++ signature :
#         unsigned long getNumberBreakpoints()
#
def getNumberBreakpoints():
    return pykd.getNumberBreakpoints()
#
# 函数getNumberProcesses
#
# getNumberProcesses() -> int :
#     Return number of processes on the target system
#
#     C++ signature :
#         unsigned long getNumberProcesses()
def getNumberProcesses():
    return pykd.getNumberProcesses()
#
#
# 函数getNumberRegisters
#
# getNumberRegisters() -> int :
#     Return a number of CPU registers
#
#     C++ signature :
#         unsigned long getNumberRegisters()
#
def getNumberRegisters():
    return pykd.getNumberRegisters()
#
# 函数getNumberThreads
#
# getNumberThreads() -> int :
#     Return number of threads on the current system
#
#     C++ signature :
#         unsigned long getNumberThreads()
def getNumberThreads():
    return pykd.getNumberThreads()
#
#
# 函数getOffset
#eax=pykdPackage.getOffset("nt!NtOpenProcess")可以获得函数的地址
# getOffset( (str)arg1) -> int :
#     Return traget virtual address for specified symbol
#
#     C++ signature :
#         unsigned __int64 getOffset(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
def getOffset(arg1):
    return pykd.getOffset(arg1)
#
# 函数getOutputMask
#
# getOutputMask() -> int :
#     Get output mask
#
#     C++ signature :
#         unsigned long getOutputMask()

def getOutputMask():
    return pykd.getOutputMask()
#
#
# 函数getParam
#
# getParam( (str)arg1) -> typedVar :
#     Get the function argument by name
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> getParam(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
def getParam(arg1):
    return pykd.getParam(arg1)
#
# 函数getParams
#
# getParams() -> list :
#     Get list of function arguments as list of tuple (name, value )
#
#     C++ signature :
#         class boost::python::list getParams()
def getParams():
    return pykd.getParams()
#
#
# 函数getProcessExeName
#
# getProcessExeName([  (int)Id]) -> str :
#     Return name of executable file of the process
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > getProcessExeName([ unsigned long])
#
def getProcessExeName(arg1):
    return pykd.getProcessExeName(arg1)
#
# 函数getProcessId
#
# getProcessId( (int)arg1) -> int :
#     Return process ID by index
#
#     C++ signature :
#         unsigned long getProcessId(unsigned long)
#
def getProcessId(arg1):
    return pykd.getProcessId(arg1)
#
# 函数getProcessIdBySystemID
#
# getProcessIdBySystemID( (int)arg1) -> int :
#     Return process ID by the system's process ID ( PID )
#
#     C++ signature :
#         unsigned long getProcessIdBySystemID(unsigned long)
#
def getProcessIdBySystemID(arg1):
    return pykd.getProcessIdBySystemID(arg1)
#
# 函数getProcessOffset
#
# getProcessOffset([  (int)Id]) -> int :
#     Return the location in the target's memory of the process structure ( PEB )
#
#     C++ signature :
#         unsigned __int64 getProcessOffset([ unsigned long])
#
def getProcessOffset(arg1):
    return pykd.getProcessOffset(arg1)
#
# 函数getProcessSystemID
#
# getProcessSystemID([  (int)Id]) -> int :
#     Return system process ID ( PID )
#
#     C++ signature :
#         unsigned long getProcessSystemID([ unsigned long])
#
def getProcessSystemID(arg1):
    return pykd.getProcessSystemID(arg1)
#
# 函数getProcessThreads
#
# getProcessThreads() -> list :
#     Get all process's threads
#
#     C++ signature :
#         class boost::python::list getProcessThreads()
#
def getProcessThreads():
    return pykd.getProcessThreads()
#
# 函数getRegisterName
#
# getRegisterName( (int)arg1) -> str :
#     Return register name by its index
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > getRegisterName(unsigned long)
#
def getRegisterName(arg1):
    return pykd.getRegisterName(arg1)
#
# 函数getSP
#
# getSP() -> int :
#     Return stack pointer
#
#     C++ signature :
#         unsigned __int64 getSP()
def getSP():
    return pykd.getSP()
#
#
# 函数getSourceFile
#
# getSourceFile([  (int)offset]) -> str :
#     Return source file by the specified offset
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > getSourceFile([ unsigned __int64])
#
def getSourceFile(arg1):
    return pykd.getSourceFile(arg1)
#
# 函数getSourceFileFromSrcSrv
#
# getSourceFileFromSrcSrv([  (int)offset]) -> str :
#     Load and return source file from source server by the specified offset
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > getSourceFileFromSrcSrv([ unsigned __int64])
#
def getSourceFileFromSrcSrv(arg1):
    return pykd.getSourceFileFromSrcSrv(arg1)
#
# 函数getSourceLine
#
# getSourceLine([  (int)offset]) -> tuple :
#     Return source file name, line and displacement by the specified offset
#
#     C++ signature :
#         class boost::python::tuple getSourceLine([ unsigned __int64])
#
def getSourceLine(arg1):
    return pykd.getSourceLine(arg1)
#
# 函数getSrcPath
#
# getSrcPath() -> str :
#     Return current source server path
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > getSrcPath()
#
def getSrcPath():
    return pykd.getSrcPath()
#
# 函数getStack
#
# getStack([  (bool)inlineFrames]) -> list :
#     Return a current stack as a list of stackFrame objects
#
#     C++ signature :
#         class boost::python::list getStack([ bool])
#
def getStack(arg1):
    return pykd.getStack(arg1)
#
# 函数getSymbolPath
#
# getSymbolPath() -> str :
#     Returns current symbol path
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > getSymbolPath()
#
def getSymbolPath():
    return pykd.getSymbolPath()
#
# 函数getSymbolProviderFromSource
#
# getSymbolProviderFromSource( (str)sourceCode [, (str)compileOptions]) -> symbolProvider :
#     Create symbol provider for source code
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::SymbolProvider> getSymbolProviderFromSource(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > [,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >])
#
def getSymbolProviderFromSource(sourceCode,compileOptions):
    return pykd.getSymbolProviderFromSource(sourceCode,compileOptions)
#
# 函数getSystemVersion
#
# getSystemVersion() -> systemVersion :
#     Return systemVersion
#
#     C++ signature :
#         struct kdlib::SystemInfo getSystemVersion()
#
def getSystemVersion():
    return pykd.getSystemVersion()
#
# 函数getTargetProcesses
#
# getTargetProcesses() -> list :
#     Get all target processes
#
#     C++ signature :
#         class boost::python::list getTargetProcesses()
#
def getTargetProcesses():
    return pykd.getTargetProcesses()
#
# 函数getThreadId
#
# getThreadId( (int)arg1) -> int :
#     Return thread id by index
#
#     C++ signature :
#         unsigned long getThreadId(unsigned long)
#
def getThreadId(arg1):
    return pykd.getThreadId(arg1)
#
# 函数getThreadIdByOffset
#
# getThreadIdByOffset( (int)arg1) -> int :
#     Return thread ID by the location in the targ et's memory of the thread structure
#
#     C++ signature :
#         unsigned long getThreadIdByOffset(unsigned __int64)
#
def getThreadIdByOffset(arg1):
    return pykd.getThreadIdByOffset(arg1)
#
# 函数getThreadIdBySystemID
#
# getThreadIdBySystemID([  (int)Tid]) -> int :
#     Return thread ID by the system's thread ID ( TID )
#
#     C++ signature :
#         unsigned long getThreadIdBySystemID([ unsigned long])
#
def getThreadIdBySystemID(arg1):
    return pykd.getThreadIdBySystemID(arg1)
#
# 函数getThreadOffset
#
# getThreadOffset([  (int)Id]) -> int :
#     Return the location in the target's memory of the thread structure ( TEB )
#
#     C++ signature :
#         unsigned __int64 getThreadOffset([ unsigned long])
#
def getThreadOffset(arg1):
    return pykd.getThreadOffset(arg1)
#
# 函数getThreadSystemID
#
# getThreadSystemID([  (int)Id]) -> int :
#     Return system thread ID ( TID )
#
#     C++ signature :
#         unsigned long getThreadSystemID([ unsigned long])
#
def getThreadSystemID(arg1):
    return pykd.getThreadSystemID(arg1)
#
# 函数getTypeFromSource
#
# getTypeFromSource( (str)sourceCode, (str)typeName [, (str)compileOptions]) -> typeInfo :
#     Create typeInfo class from C/C++ source code
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> getTypeFromSource(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > [,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >])
#

#
# 函数getTypeInfoProviderFromPdb
#
# getTypeInfoProviderFromPdb( (str)filePath [, (int)baseOffset]) -> typeInfoProvider :
#     Create typeInfo provider from  pdb file
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfoProvider> getTypeInfoProviderFromPdb(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > [,unsigned __int64])
#
#
# 函数getTypeInfoProviderFromSource
#
# getTypeInfoProviderFromSource( (str)sourceCode [, (str)compileOptions]) -> typeInfoProvider :
#     Create typeInfo provider from  C/C++ source code
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfoProvider> getTypeInfoProviderFromSource(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > [,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >])
#
#
# 函数getVaProtect
#
# getVaProtect( (int)arg1) -> memoryProtect :
#     Return memory attributes
#
#     C++ signature :
#         enum kdlib::MemoryProtect getVaProtect(unsigned __int64)
#
def getVaProtect(arg1):
    return pykd.getVaProtect(arg1)
#
# 功能去
#
# go() -> executionStatus :
#     Go debugging
#
#     C++ signature :
#         enum kdlib::ExecutionStatus go()
#
def go():
    return pykd.go()
#
# 函数初始化
#
# initialize() -> None :
#     Initialize local debug engine, only for console mode
#
#     C++ signature :
#         void initialize()
#
#
# 功能是64位系统
#
# is64bitSystem() -> bool :
#     Check if target system has 64 address space
#
#     C++ signature :
#         bool is64bitSystem()
#
def is64bitSystem():
    return pykd.is64bitSystem()
#
# 函数isDumpAnalyzing
#
# isDumpAnalyzing() -> bool :
#     Check if it is a dump analyzing ( not living debuggee )
#
#     C++ signature :
#         bool isDumpAnalyzing()
#
def isDumpAnalyzing():
    return pykd.isDumpAnalyzing()
#
# 函数isKernelDebugging
#
# isKernelDebugging() -> bool :
#     Check if kernel dubugging is running
#
#     C++ signature :
#         bool isKernelDebugging()
#
def isKernelDebugging():
    return pykd.isKernelDebugging()
#
# 函数isLocalKernelDebuggerEnabled
#
# isLocalKernelDebuggerEnabled() -> bool :
#     Check whether kernel debugging is enabled for the local kernel
#
#     C++ signature :
#         bool isLocalKernelDebuggerEnabled()
#
def isLocalKernelDebuggerEnabled():
    return pykd.isLocalKernelDebuggerEnabled()
#
# 函数isVaRegionValid
#
# isVaRegionValid( (int)arg1, (int)arg2) -> bool :
#     Check if the virtaul addresses region is valid
#
#     C++ signature :
#         bool isVaRegionValid(unsigned __int64,unsigned long)
#
def isVaRegionValid(addr,len):
    return pykd.isVaRegionValid(addr,len)
#
# 函数isValid
#
# isValid( (int)arg1) -> bool :
#     Check if the virtual address is valid
#
#     C++ signature :
#         bool isValid(unsigned __int64)
#
def isValid(addr):
    return pykd.isValid(addr)
#
# 函数isWindbgExt
#
# isWindbgExt() -> bool :
#     Check if script works in windbg context
#
#     C++ signature :
#         bool isWindbgExt()
def isWindbgExt():
    return pykd.isWindbgExt()
#
#
# 函数killAllProcesses
#
# killAllProcesses() -> None :
#     Detach from all process then terminate them
#
#     C++ signature :
#         void killAllProcesses()
#
def killAllProcesses():
    return pykd.killAllProcesses()
#
# 功能killProcess
#
# killProcess([  (int)id]) -> None :
#     Stop debugging and terminate current process
#
#     C++ signature :
#         void killProcess([ unsigned long])
#
def killProcess(pid):
    return pykd.killProcess(pid)
#
# 函数loadAnsiString
#
# loadAnsiString( (int)arg1) -> str :
#     Return string represention of windows ANSI_STRING type
#
#     C++ signature :
#         class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > loadAnsiString(unsigned __int64)
#
def loadAnsiString(addr):
    return pykd.loadAnsiString(addr)
#
# 函数loadBytes
#
# loadBytes( (int)offset, (int)count [, (bool)phyAddr]) -> list :
#     Read the block of the target's memory and return it as list of unsigned bytes
#
#     C++ signature :
#         class boost::python::list loadBytes(unsigned __int64,unsigned long [,bool])
#
def loadBytes(addr,len,**args):
    return pykd.loadBytes(addr,len,**args)
#
# 函数loadCStr
#
# loadCStr( (int)arg1) -> str :
#     Load string from the target buffer containing 0-terminated ansi-string
#
#     C++ signature :
#         class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > loadCStr(unsigned __int64)
#
def loadCStr(addr):
    return pykd.loadCStr(addr)
#
# 函数loadChars
#
# loadChars( (int)address, (int)count [, (bool)phyAddr]) -> str :
#     Load string from target memory
#
#     C++ signature :
#         class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > loadChars(unsigned __int64,unsigned long [,bool])
#
def loadChars(addr,count,**args):
    return pykd.loadChars(addr,count,**args)
#
# 函数loadDWords
#
# loadDWords( (int)offset, (int)count [, (bool)phyAddr]) -> list :
#     Read the block of the target's memory and return it as list of unsigned long ( double word )
#
#     C++ signature :
#         class boost::python::list loadDWords(unsigned __int64,unsigned long [,bool])
#
def loadDWords(addr,count,**args):
    return pykd.loadDWords(addr,count,**args)
#
# 函数loadDoubles
#
# loadDoubles( (int)offset, (int)count [, (bool)phyAddr]) -> list :
#     Read the block of the target's memory and return it as list of doubles
#
#     C++ signature :
#         class boost::python::list loadDoubles(unsigned __int64,unsigned long [,bool])
#
def loadDoubles(addr,count,**args):
    return pykd.loadDoubles(addr,count,**args)
#
# 函数loadDump
#
# loadDump( (str)arg1) -> int :
#     Load crash dump
#
#     C++ signature :
#         unsigned long loadDump(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
def loadDump(arg1):
    return pykd.loadDump(arg1)
#
# 函数loadExt
#
# loadExt( (str)arg1) -> int :
#     Load a WinDBG extension. Return handle of the loaded extension
#
#     C++ signature :
#         unsigned __int64 loadExt(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
def loadExt(arg1):
    return pykd.loadExt(arg1)
#
# 函数loadFloats
#
# loadFloats( (int)offset, (int)count [, (bool)phyAddr]) -> list :
#     Read the block of the target's memory and return it as list of floats
#
#     C++ signature :
#         class boost::python::list loadFloats(unsigned __int64,unsigned long [,bool])
#
def loadFloats(addr,count,**args):
    return pykd.loadFloats(addr,count,**args)
#
# 函数loadPtrList
#
# loadPtrList( (int)arg1) -> list :
#     Return list of pointers, each points to next
#
#     C++ signature :
#         class boost::python::list loadPtrList(unsigned __int64)
#
def loadPtrList(addr):
    return pykd.loadPtrList(addr)
#
# 函数loadPtrs
#
# loadPtrs( (int)arg1, (int)arg2) -> list :
#     Read the block of the target's memory and return it as a list of pointers
#
#     C++ signature :
#         class boost::python::list loadPtrs(unsigned __int64,unsigned long)
#
def loadPtrs(start,end):
    return pykd.loadPtrs(start,end)
#
# 函数loadQWords
#
# loadQWords( (int)offset, (int)count [, (bool)phyAddr]) -> list :
#     Read the block of the target's memory and return it as list of unsigned long long ( quad word )
#
#     C++ signature :
#         class boost::python::list loadQWords(unsigned __int64,unsigned long [,bool])
#
def loadQWords(addr,count,**args):
    return pykd.loadQWords(addr,count,**args)
#
# 函数loadSignBytes
#
# loadSignBytes( (int)offset, (int)count [, (bool)phyAddr]) -> list :
#     Read the block of the target's memory and return it as list of signed bytes
#
#     C++ signature :
#         class boost::python::list loadSignBytes(unsigned __int64,unsigned long [,bool])
#
def loadSignBytes(addr,count,**args):
    return pykd.loadSignBytes(addr,count,**args)
#
# 函数loadSignDWords
#
# loadSignDWords( (int)offset, (int)count [, (bool)phyAddr]) -> list :
#     Read the block of the target's memory and return it as list of signed longs
#
#     C++ signature :
#         class boost::python::list loadSignDWords(unsigned __int64,unsigned long [,bool])
#
def loadSignDWords(addr,count,**args):
    return pykd.loadSignDWords(addr,count,**args)
#
# 函数loadSignQWords
#
# loadSignQWords( (int)offset, (int)count [, (bool)phyAddr]) -> list :
#     Read the block of the target's memory and return it as list of signed long longs
#
#     C++ signature :
#         class boost::python::list loadSignQWords(unsigned __int64,unsigned long [,bool])
#
def loadSignQWords(addr,count,**args):
    return pykd.loadSignQWords(addr,count,**args)
#
# 函数loadSignWords
#
# loadSignWords( (int)offset, (int)count [, (bool)phyAddr]) -> list :
#     Read the block of the target's memory and return it as list of signed words
#
#     C++ signature :
#         class boost::python::list loadSignWords(unsigned __int64,unsigned long [,bool])
#
def loadSignWords(addr,count,**args):
    return pykd.loadSignWords(addr,count,**args)
#
# 函数loadTaggedBuffer
#
# loadTaggedBuffer( (str)arg1) -> list :
#     Read the buffer of secondary callback data by ID
#
#     C++ signature :
#         class boost::python::list loadTaggedBuffer(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
def loadTaggedBuffer(addr):
    return pykd.loadTaggedBuffer(addr)
#
# 函数loadUnicodeString
#
# loadUnicodeString( (int)arg1) -> str :
#     Return string represention of windows UNICODE_STRING type
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > loadUnicodeString(unsigned __int64)
#
def loadUnicodeString(addr):
    return pykd.loadUnicodeString(addr)
#
# 函数loadWChars
#
# loadWChars( (int)address, (int)count [, (bool)phyAddr]) -> str :
#     Load string from target memory
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > loadWChars(unsigned __int64,unsigned long [,bool])
def loadWChars(addr,count,**args):
    return pykd.loadWChars(addr,count,**args)
#
# 函数loadWStr
#
# loadWStr( (int)arg1) -> str :
#     Load string from the target buffer containing 0-terminated unicode-string
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > loadWStr(unsigned __int64)
#
def loadWStr(addr):
    return pykd.loadWStr(addr)
#
# 功能loadWords
#
# loadWords( (int)offset, (int)count [, (bool)phyAddr]) -> list :
#     Read the block of the target's memory and return it as list of unsigned shorts
#
#     C++ signature :
#         class boost::python::list loadWords(unsigned __int64,unsigned long [,bool])
#
def loadWords(addr,count,**args):
    return pykd.loadWords(addr,count,**args)
#
# 功能页面大小
#
# pageSize() -> int :
#     Get the page size for the currently executing processor context
#
#     C++ signature :
#         unsigned __int64 pageSize()
def pageSize():
    return pykd.pageSize()
#
#
# 功能popStack
#
# popStack() -> object :
#     Pop a value from a stack
#
#     C++ signature :
#         class kdlib::NumVariant popStack()
#
def popStack():
    return pykd.popStack()
#
# 函数ptrByte
#
# ptrByte( (int)arg1) -> int :
#     Read an unsigned 1-byte integer from the target memory
#
#     C++ signature :
#         unsigned char ptrByte(unsigned __int64)
#
def ptrByte(addr):
    return pykd.ptrByte(addr)
#
# 函数ptrDWord
#
# ptrDWord( (int)arg1) -> int :
#     Read an unsigned 4-byte integer from the target memory
#
#     C++ signature :
#         unsigned long ptrDWord(unsigned __int64)
#
def ptrDWord(addr):
    return pykd.ptrDWord(addr)
#
# 函数ptrDouble
#
# ptrDouble( (int)arg1) -> float :
#     Read a float with single precision from the target memory
#
#     C++ signature :
#         double ptrDouble(unsigned __int64)
#
def ptrDouble(addr):
    return pykd.ptrDouble(addr)
#
# 函数ptrFloat
#
# ptrFloat( (int)arg1) -> float :
#     Read a float with single precision from the target memory
#
#     C++ signature :
#         float ptrFloat(unsigned __int64)
#
def ptrFloat(addr):
    return pykd.ptrFloat(addr)
#
# 函数ptrMWord
#
# ptrMWord( (int)arg1) -> int :
#     Read an unsigned mashine's word wide integer from the target memory
#
#     C++ signature :
#         unsigned __int64 ptrMWord(unsigned __int64)
#
def ptrMWord(addr):
    return pykd.ptrMWord(addr)
#
# 函数ptrPtr
#
# ptrPtr( (int)arg1) -> int :
#     Read an pointer value from the target memory
#
#     C++ signature :
#         unsigned __int64 ptrPtr(unsigned __int64)
#
def ptrPtr(addr):
    return pykd.ptrPtr(addr)
#
# 函数ptrQWord
#
# ptrQWord( (int)arg1) -> int :
#     Read an unsigned 8-byte integer from the target memory
#
#     C++ signature :
#         unsigned __int64 ptrQWord(unsigned __int64)
#
def ptrQWord(addr):
    return pykd.ptrQWord(addr)
#
# 函数ptrSignByte
#
# ptrSignByte( (int)arg1) -> int :
#     Read an signed 1-byte integer from the target memory
#
#     C++ signature :
#         int ptrSignByte(unsigned __int64)
#
def ptrSignByte(addr):
    return pykd.ptrSignByte(addr)
#
# 函数ptrSignDWord
#
# ptrSignDWord( (int)arg1) -> int :
#     Read an signed 4-byte integer from the target memory
#
#     C++ signature :
#         long ptrSignDWord(unsigned __int64)
#
def ptrSignDWord(addr):
    return pykd.ptrSignDWord(addr)
#
# 函数ptrSignMWord
#
# ptrSignMWord( (int)arg1) -> int :
#     Read an signed mashine's word wide integer from the target memory
#
#     C++ signature :
#         __int64 ptrSignMWord(unsigned __int64)
#
def ptrSignMWord(addr):
    return pykd.ptrSignMWord(addr)
#
# 函数ptrSignQWord
#
# ptrSignQWord( (int)arg1) -> int :
#     Read an signed 8-byte integer from the target memory
#
#     C++ signature :
#         __int64 ptrSignQWord(unsigned __int64)
#
def ptrSignQWord(addr):
    return pykd.ptrSignQWord(addr)
#
# 函数ptrSignWord
#
# ptrSignWord( (int)arg1) -> int :
#     Read an signed 2-byte integer from the target memory
#
#     C++ signature :
#         short ptrSignWord(unsigned __int64)
#
def ptrSignWord(addr):
    return pykd.ptrSignWord(addr)
# 函数ptrSize
#
# ptrSize() -> int :
#     Return effective pointer size
#
#     C++ signature :
#         unsigned __int64 ptrSize()
#
#
def ptrSize():
    return pykd.ptrSize()
# 函数ptrWord
#
# ptrWord( (int)arg1) -> int :
#     Read an unsigned 2-byte integer from the target memory
#
#     C++ signature :
#         unsigned short ptrWord(unsigned __int64)
#
#
# 函数pushStack
#
# pushStack( (object)arg1) -> None :
#     Push a value into a stack
#
#     C++ signature :
#         void pushStack(class kdlib::NumVariant)
#
#
# 函数rdmsr
#
# rdmsr( (int)arg1) -> int :
#     Return MSR value
#
#     C++ signature :
#         unsigned __int64 rdmsr(unsigned long)
#
def rdmsr(arg1):
    return pykd.rdmsr(arg1)
#
# 功能寄存器
#
# reg( (str)arg1) -> object :
#     Return a CPU regsiter value by the register's name
#
#     C++ signature :
#         class boost::python::api::object reg(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
# reg( (int)arg1) -> object :
#     Return a CPU register value by the register's number
#
#     C++ signature :
#         class boost::python::api::object reg(unsigned long)
#
def reg(arg1):
    return pykd.reg(arg1)
#
# 功能remoteConnect
#
# remoteConnect( (str)arg1) -> None :
#     Initialize debug engine for remoting, only for console mode
#
#     C++ signature :
#         void remoteConnect(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 函数removeAllBp
#
# removeAllBp() -> None :
#     Remove all breakpoints
#
#     C++ signature :
#         void removeAllBp()
#
def removeAllBp():
    return pykd.removeAllBp()
#
# 功能removeBp
#
# removeBp( (int)arg1) -> None :
#     Remove breakpoint by index
#
#     C++ signature :
#         void removeBp(unsigned long)
#
def removeBp(arg1):
    return pykd.removeBp(arg1)
#
# 功能removeExt
#
# removeExt( (int)arg1) -> None :
#     Unload a WinDBG extension. Parameter: handle returned by loadExt
#
#     C++ signature :
#         void removeExt(unsigned __int64)
#
# removeExt( (str)arg1) -> None :
#     Unload a WinDBG extension. Parameter: extension path
#
#     C++ signature :
#         void removeExt(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
def removeExt(arg1):
    return pykd.removeExt(arg1)
#
# 函数removeSyntheticModule
#
# removeSyntheticModule( (int)arg1) -> None :
#     The removeSyntheticModule function removes a synthetic module from the module list the debugger maintains for the current process
#
#     C++ signature :
#         void removeSyntheticModule(unsigned __int64)
#
#
# 函数removeSyntheticSymbol
#
# removeSyntheticSymbol( (syntheticSymbol)arg1) -> None :
#     The removeSyntheticSymbol function removes a synthetic symbol from a module in the current proces
#
#     C++ signature :
#         void removeSyntheticSymbol(struct kdlib::SyntheticSymbol)
#
#
# 功能resetFrame
#
# resetFrame() -> None :
#     Resets the current local scope to the default scope of the current thread
#
#     C++ signature :
#         void resetFrame()
def resetFrame():
    return pykd.resetFrame()
#
#
# 功能searchMemory
#
# searchMemory( (int)arg1, (int)arg2, (list)arg3) -> int :
#     Search in virtual memory
#
#     C++ signature :
#         unsigned __int64 searchMemory(unsigned __int64,unsigned long,class boost::python::list)
#
# searchMemory( (int)arg1, (int)arg2, (str)arg3) -> int :
#     Search in virtual memory
#
#     C++ signature :
#         unsigned __int64 searchMemory(unsigned __int64,unsigned long,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
#
def searchMemory(start,end,content):
    return pykd.searchMemory(start,end,content)
#
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
#
# 函数setByte
#
# setByte( (int)arg1, (int)arg2) -> None :
#     Write an unsigned 1-byte integer to the target memory
#
#     C++ signature :
#         void setByte(unsigned __int64,unsigned char)
#
#
# 功能setCPUMode
#
# setCPUMode( (CPUType)arg1) -> None :
#     Set current processor mode (CPUType)
#
#     C++ signature :
#         void setCPUMode(enum kdlib::CPUType)
#
#
# 函数setCurrentProcess
#
# setCurrentProcess( (int)arg1) -> None :
#     Set current process
#
#     C++ signature :
#         void setCurrentProcess(unsigned __int64)
#
#
# 函数setCurrentProcessId
#
# setCurrentProcessId( (int)arg1) -> None :
#     Set current process by debug ID
#
#     C++ signature :
#         void setCurrentProcessId(unsigned long)
#
#
# 函数setCurrentThread
#
# setCurrentThread( (int)arg1) -> None :
#     Set current thread
#
#     C++ signature :
#         void setCurrentThread(unsigned __int64)
#
#
# 函数setCurrentThreadId
#
# setCurrentThreadId( (int)arg1) -> None :
#     Set current thread by debug ID
#
#     C++ signature :
#         void setCurrentThreadId(unsigned long)
#
#
# 函数setDWord
#
# setDWord( (int)arg1, (int)arg2) -> None :
#     Write an unsigned 4-byte integer to the target memory
#
#     C++ signature :
#         void setDWord(unsigned __int64,unsigned long)
#
#
# 功能集Double
#
# setDouble( (int)arg1, (float)arg2) -> None :
#     Write a float with single precision to the target memory
#
#     C++ signature :
#         void setDouble(unsigned __int64,double)
#
#
# 功能setFP
#
# setFP( (int)arg1) -> None :
#     Change frame pointer
#
#     C++ signature :
#         void setFP(unsigned __int64)
#
#
# 函数setFloat
#
# setFloat( (int)arg1, (float)arg2) -> None :
#     Write a float with single precision to the target memory
#
#     C++ signature :
#         void setFloat(unsigned __int64,float)
#
#
# 函数setFrame
#
# setFrame( (stackFrame)arg1) -> None :
#     Change current local scope
#
#     C++ signature :
#         void setFrame(class boost::shared_ptr<class kdlib::StackFrame> {lvalue})
#
# setFrame( (int)arg1) -> None :
#     Change current local scope
#
#     C++ signature :
#         void setFrame(unsigned long)
#
#
# 功能setIP
#
# setIP( (int)arg1) -> None :
#     Change instruction pointer
#
#     C++ signature :
#         void setIP(unsigned __int64)
#
#
# 函数setImplicitProcess
#
# setImplicitProcess( (int)arg1) -> None :
#     Set implicit process
#
#     C++ signature :
#         void setImplicitProcess(unsigned __int64)
#
#
# 函数setImplicitThread
#
# setImplicitThread( (int)arg1) -> None :
#     Set implicit thread
#
#     C++ signature :
#         void setImplicitThread(unsigned __int64)
#
#
# 函数setOutputMask
#
# setOutputMask( (int)arg1) -> None :
#     Set output mask
#
#     C++ signature :
#         void setOutputMask(unsigned long)
#
#
# 函数setPtr
#
# setPtr( (int)arg1, (int)arg2) -> None :
#     Write an pointer value to the target memory
#
#     C++ signature :
#         void setPtr(unsigned __int64,unsigned __int64)
#
#
# 函数setQWord
#
# setQWord( (int)arg1, (int)arg2) -> None :
#     Write an unsigned 8-byte integer to the target memory
#
#     C++ signature :
#         void setQWord(unsigned __int64,unsigned __int64)
#
#
# 函数setReg
#
# setReg( (str)arg1, (object)arg2) -> None :
#     Set a CPU register value by its name
#
#     C++ signature :
#         void setReg(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >,class boost::python::api::object)
#
# setReg( (int)arg1, (object)arg2) -> None :
#     Set a CPU register value by its index
#
#     C++ signature :
#         void setReg(unsigned long,class boost::python::api::object)
#
#
# 功能集SP
#
# setSP( (int)arg1) -> None :
#     Change stack pointer
#
#     C++ signature :
#         void setSP(unsigned __int64)
#
#
# 函数setSignByte
#
# setSignByte( (int)arg1, (int)arg2) -> None :
#     Write an signed 1-byte integer to the target memory
#
#     C++ signature :
#         void setSignByte(unsigned __int64,int)
#
#
# 函数setSignDWord
#
# setSignDWord( (int)arg1, (int)arg2) -> None :
#     Write an signed 4-byte integer to the target memory
#
#     C++ signature :
#         void setSignDWord(unsigned __int64,long)
#
#
# 函数setSignQWord
#
# setSignQWord( (int)arg1, (int)arg2) -> None :
#     Write an signed 8-byte integer to the target memory
#
#     C++ signature :
#         void setSignQWord(unsigned __int64,__int64)
#
#
# 函数setSignWord
#
# setSignWord( (int)arg1, (int)arg2) -> None :
#     Write an signed 2-byte integer to the target memory
#
#     C++ signature :
#         void setSignWord(unsigned __int64,short)
#
#
# 函数setSrcPath
#
# setSrcPath( (str)arg1) -> None :
#     Set source path
#
#     C++ signature :
#         void setSrcPath(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 函数setStatusMessage
#
# setStatusMessage( (str)arg1) -> None :
#     Set message at a windbg status bar
#
#     C++ signature :
#         void setStatusMessage(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 函数setSymSrvDir
#
# setSymSrvDir( (str)arg1) -> None :
#     Set directory of SYMSRV.dll library.
#     Usually this is a directory of WinDbg
#
#     C++ signature :
#         void setSymSrvDir(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 函数setSymbolPath
#
# setSymbolPath( (str)arg1) -> None :
#     Set current symbol path
#
#     C++ signature :
#         void setSymbolPath(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 功能集词
#
# setWord( (int)arg1, (int)arg2) -> None :
#     Write an unsigned 2-byte integer to the target memory
#
#     C++ signature :
#         void setWord(unsigned __int64,unsigned short)
#
#
# 函数sizeof
#
# sizeof( (str)arg1) -> int :
#     Return a size of the type or variable
#
#     C++ signature :
#         unsigned __int64 sizeof(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 函数源Step
#
# sourceStep() -> executionStatus :
#     The target is executing a single source line
#
#     C++ signature :
#         enum kdlib::ExecutionStatus sourceStep()
#
#
# 函数sourceStepOver
#
# sourceStepOver() -> executionStatus :
#     The target is executing a single source line
#
#     C++ signature :
#         enum kdlib::ExecutionStatus sourceStepOver()
#
#
# 函数stackAlloc
#
# stackAlloc( (int)arg1) -> int :
#     Allocate bytes of space in the stack in the target process
#
#     C++ signature :
#         unsigned __int64 stackAlloc(unsigned short)
#
#
# 功能栈免费
#
# stackFree( (int)arg1) -> int :
#     Free space in the stack previously allocated by stackAlloc
#
#     C++ signature :
#         unsigned __int64 stackFree(unsigned short)
#
#
# 函数startProcess
#
# startProcess( (str)commandline [, (int)debugOptions]) -> int :
#     Start process for debugging
#
#     C++ signature :
#         unsigned long startProcess(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > [,unsigned long])
#
#
# 功能步骤
#
# step() -> executionStatus :
#     The target is executing a single instruction or--if that instruction is a subroutine call--subroutine
#
#     C++ signature :
#         enum kdlib::ExecutionStatus step()
#
#
# 功能分步
#
# stepout() -> executionStatus :
#     The traget is executing while not returned from the current subroutine
#
#     C++ signature :
#         enum kdlib::ExecutionStatus stepout()
#
#
# 功能开关CPU模式
#
# switchCPUMode() -> None :
#     Switch processor mode ( X86 <-> X64 )
#
#     C++ signature :
#         void switchCPUMode()
#
#
# 功能系统正常运行时间
#
# systemUptime() -> int :
#     Return the number of seconds the computer has been running
#
#     C++ signature :
#         unsigned long systemUptime()
#
#
# 功能追踪
#
# trace() -> executionStatus :
#     The target is executing a single instruction
#
#     C++ signature :
#         enum kdlib::ExecutionStatus trace()
#
def trace():
    return pykd.trace()
#
# 函数类型为VarArray
#
# typedVarArray( (int)arg1, (str)arg2, (int)arg3) -> list :
#     Return a list of the typedVar class instances. Each item represents an item of the counted array in the target memory
#
#     C++ signature :
#         class boost::python::list typedVarArray(unsigned __int64,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >,unsigned __int64)
#
# typedVarArray( (int)arg1, (typeInfo)arg2, (int)arg3) -> list :
#     Return a list of the typedVar class instances. Each item represents an item of the counted array in the target memory
#
#     C++ signature :
#         class boost::python::list typedVarArray(unsigned __int64,class boost::shared_ptr<class kdlib::TypeInfo> {lvalue},unsigned __int64)
#
#
# 函数类型为VarList
#
# typedVarList( (int)arg1, (str)arg2, (str)arg3) -> list :
#     Return a list of the typedVar class instances. Each item represents an item of the linked list in the target memory
#
#     C++ signature :
#         class boost::python::list typedVarList(unsigned __int64,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
# typedVarList( (int)arg1, (typeInfo)arg2, (str)arg3) -> list :
#     Return a list of the typedVar class instances. Each item represents an item of the linked list in the target memory
#
#     C++ signature :
#         class boost::python::list typedVarList(unsigned __int64,class boost::shared_ptr<class kdlib::TypeInfo> {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 函数writeBytes
#
# writeBytes( (int)offset, (list)values [, (bool)phyAddr]) -> None :
#     Writing a list of unsigned bytes to the target's memory
#
#     C++ signature :
#         void writeBytes(unsigned __int64,class boost::python::list [,bool])
#
#
# 函数writeCStr
#
# writeCStr( (int)arg1, (str)arg2) -> None :
#     Write string as a 0 terminated ansi string to the buffer
#
#     C++ signature :
#         void writeCStr(unsigned __int64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
#
#
# 函数writeDWords
#
# writeDWords( (int)offset, (list)values [, (bool)phyAddr]) -> None :
#     Writing a list of unsigned long ( double word ) to the target's memory
#
#     C++ signature :
#         void writeDWords(unsigned __int64,class boost::python::list [,bool])
#
#
# 函数writeDoubles
#
# writeDoubles( (int)offset, (list)values [, (bool)phyAddr]) -> None :
#     Writing a list of doubles to the target's memory
#
#     C++ signature :
#         void writeDoubles(unsigned __int64,class boost::python::list [,bool])
#
#
# 函数writeDump
#
# writeDump( (str)arg1, (bool)arg2) -> None :
#     Create memory dump file
#
#     C++ signature :
#         void writeDump(class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >,bool)
#
#
# 函数writeFloats
#
# writeFloats( (int)offset, (list)values [, (bool)phyAddr]) -> None :
#     Writing a list of floats to the target's memory
#
#     C++ signature :
#         void writeFloats(unsigned __int64,class boost::python::list [,bool])
#
#
# 函数writeQWords
#
# writeQWords( (int)offset, (list)values [, (bool)phyAddr]) -> None :
#     Writing a list of unsigned long long ( quad word ) to the target's memory
#
#     C++ signature :
#         void writeQWords(unsigned __int64,class boost::python::list [,bool])
#
#
# 函数writeSignBytes
#
# writeSignBytes( (int)offset, (list)values [, (bool)phyAddr]) -> None :
#     Writing a list of signed bytes to the target's memory
#
#     C++ signature :
#         void writeSignBytes(unsigned __int64,class boost::python::list [,bool])
#
#
# 函数writeSignDWords
#
# writeSignDWords( (int)offset, (list)values [, (bool)phyAddr]) -> None :
#     Writing a list of signed longs to the target's memory
#
#     C++ signature :
#         void writeSignDWords(unsigned __int64,class boost::python::list [,bool])
#
#
# 函数writeSignQWords
#
# writeSignQWords( (int)offset, (list)values [, (bool)phyAddr]) -> None :
#     Writing a list of signed long longs to the target's memory
#
#     C++ signature :
#         void writeSignQWords(unsigned __int64,class boost::python::list [,bool])
#
#
# 函数writeSignWords
#
# writeSignWords( (int)offset, (list)count [, (bool)phyAddr]) -> None :
#     Writing a list of signed words to the target's memory
#
#     C++ signature :
#         void writeSignWords(unsigned __int64,class boost::python::list [,bool])
#
#
# 函数writeWStr
#
# writeWStr( (int)arg1, (str)arg2) -> None :
#     Write string as a 0 terminated unicode string to the buffer
#
#     C++ signature :
#         void writeWStr(unsigned __int64,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 函数writeWords
#
# writeWords( (int)offset, (list)values [, (bool)phyAddr]) -> None :
#     Writing a list of unsigned shorts to the target's memory
#
#     C++ signature :
#         void writeWords(unsigned __int64,class boost::python::list [,bool])
#
#
# 函数wrmsr
#
# wrmsr( (int)arg1, (int)arg2) -> None :
#     Set MSR value
#
#     C++ signature :
#         void wrmsr(unsigned long,unsigned __int64)
#
#
# 类CPUException
# CPU exception
#
# 基类：
# DbgException
#
#
# 类CPUType
# type of CPU
#
# 基类：
# 枚举
#
# 值：
#
# I386：0
# AMD64：1
# ARM64：2
# 手臂：3
#
#
#
# 类CallException
# Function call exception
#
# 基类：
# DbgException
#
#
# 类DbgException
# Pykd base exception class
#
# 基类：
# 例外
#
#
# 类FileFlag
# Attributes of the file
#
# 基类：
# 枚举
#
# 值：
#
# 调试：1
# 预发布：2
# 已修补：4
# 私人建筑物：8
# 信息推断：16
# 特殊建设：32
#
#
#
# 类FixedFileInfo
# Version information for a file
#
# 基类：
# 实例
#
# 特性：
#
# FileDateLS
# FileDateMS
# FileFlags
# FileFlagsMask
# 文件操作系统
# FileSubtype
# 文件类型
# FileVersionLS
# FileVersionMS
# 产品版本LS
# 产品版本MS
# 签名
# 结构版本
#
#
#
# 属性FixedFileInfo.FileDateLS
# The least significant 32 bits of the file's 64-bit binary creation date and time stamp
#
#
# 属性FixedFileInfo.FileDateMS
# The most significant 32 bits of the file's 64-bit binary creation date and time stamp
#
#
# 属性FixedFileInfo.FileFlags
# Contains a bitmask that specifies the Boolean attributes of the file: FileFlag
#
#
# 属性FixedFileInfo.FileFlagsMask
# Contains a bitmask that specifies the valid bits in FileFlags
#
#
# 属性FixedFileInfo.FileOS
# The operating system for which this file was designed
#
#
# 属性FixedFileInfo.FileSubtype
# The function of the file. The possible values depend on the value of FileType
#
#
# 属性FixedFileInfo.FileType
# The general type of file
#
#
# 属性FixedFileInfo.FileVersionLS
# The least significant 32 bits of the file's binary version number
#
#
# 属性FixedFileInfo.FileVersionMS
# The most significant 32 bits of the file's binary version number
#
#
# 属性FixedFileInfo.ProductVersionLS
# The least significant 32 bits of the binary version number of the product with which this file was distributed
#
#
# 属性FixedFileInfo.ProductVersionMS
# The most significant 32 bits of the binary version number of the product with which this file was distributed
#
#
# 属性FixedFileInfo.Signature
# Contains the value 0xFEEF04BD
#
#
# 属性FixedFileInfo.StrucVersion
# The binary version number of this structure
#
#
# 上课地点
# Location of a varibale
#
# 基类：
# 枚举
#
# 值：
#
# 注册：2
# 内存1
#
#
#
# 类MemoryException
# Target memory access exception class
#
# 基类：
# DbgException
#
#
# 类ProcessDebugOptions
# Process debug option
#
# 基类：
# 枚举
#
# 值：
#
# BreakOnStart：1
# BreakOnStop：2
# DebugChildren：4
# NoDebugHeap：8
# 聋子：1
#
#
#
# 类SymbolException
# Symbol exception
#
# 基类：
# DbgException
#
#
# 类TypeException
# type exception
#
# 基类：
# SymbolException
#
#
# 类baseTypes
# base types enumeration
#
# 基类：
# 实例
#
#
# 类断点
# class for CPU context representation
#
# 基类：
# 实例
#
# 方法：
#
# __在里面__
# 分离
# getId
# getOffset
# onHit
# 去掉
#
#
#
# 方法断点
#
# __init__( (object)arg1, (int)arg2) -> None :
#
#     C++ signature :
#         void __init__(struct _object * __ptr64,unsigned __int64)
#
# __init__( (object)arg1, (int)arg2, (int)arg3, (int)arg4) -> None :
#
#     C++ signature :
#         void __init__(struct _object * __ptr64,unsigned __int64,unsigned __int64,unsigned long)
#
#
# 方法breakpoint.detach
#
# detach( (breakpoint)arg1) -> breakpoint :
#     detach breakpoint
#
#     C++ signature :
#         class pykd::Breakpoint * __ptr64 detach(class pykd::Breakpoint {lvalue})
#
#
# 方法breakpoint.getId
#
# getId( (breakpoint)arg1) -> int :
#     Return breakpoint ID
#
#     C++ signature :
#         unsigned long getId(class pykd::Breakpoint {lvalue})
#
#
# 方法breakpoint.getOffset
#
# getOffset( (breakpoint)arg1) -> int :
#     Return breakpoint's memory offset
#
#     C++ signature :
#         unsigned __int64 getOffset(class pykd::Breakpoint {lvalue})
#
#
# 方法断点
#
# onHit( (breakpoint)arg1) -> eventResult :
#     Breakpoint hit callback
#
#     C++ signature :
#         enum kdlib::DebugCallbackResult onHit(class pykd::Breakpoint {lvalue})
#
#
# 方法breakpoint.remove
#
# remove( (breakpoint)arg1) -> None :
#     Remove breakpoint
#
#     C++ signature :
#         void remove(class pykd::Breakpoint {lvalue})
#
#
# 类断点访问
# Breakpoint access types
#
# 基类：
# 枚举
#
# 值：
#
# 读：1
# 写：2
# 执行：4
#
#
#
# 类调用公约
# Calling convention for a function
#
# 基类：
# 枚举
#
# 值：
#
# NearC：0
# FarC：1
# 近帕斯卡：2
# 帕斯卡：3
# NearFast：4
# 极速：5
# 跳过：6
# NearStd：7
# FarStd0：8
# NearSys：9
# FarSys的：10
# 通话次数：11
# 通话次数：12
# 通用：13
# AlphaCall：14
# PpcCall：15
# 呼唤电话：16
# 紧急呼叫：17
# Am33通话：18
# TriCall：19
# Sh5通话：20
# M32R电话：21
# 电话：22
# 内联：23
#
#
#
# 类CPU
# class for CPU context representation
#
# 基类：
# 实例
#
# 特性：
#
# fp
# ip
# SP
#
#
# 方法：
#
# __getattr__
# __getitem__
# __在里面__
# __len__
# getCPUMode
# getCPUType
#
#
#
# 方法cpu .__ getattr__
#
# __getattr__( (cpu)arg1, (str)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __getattr__(class pykd::CPUContextAdapter {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法cpu .__ getitem__
#
# __getitem__( (cpu)arg1, (int)arg2) -> tuple :
#
#     C++ signature :
#         class boost::python::tuple __getitem__(class pykd::CPUContextAdapter {lvalue},unsigned long)
#
#
# 方法cpu .__ init__
#
# __init__( (object)arg1) -> None :
#
#     C++ signature :
#         void __init__(struct _object * __ptr64)
#
#
# 方法cpu .__ len__
#
# __len__( (cpu)arg1) -> int :
#
#     C++ signature :
#         unsigned long __len__(class pykd::CPUContextAdapter {lvalue})
#
#
# 方法cpu.getCPUMode
#
# getCPUMode( (cpu)arg1) -> CPUType :
#
#     C++ signature :
#         enum kdlib::CPUType getCPUMode(class pykd::CPUContextAdapter {lvalue})
#
#
# 方法cpu.getCPUType
#
# getCPUType( (cpu)arg1) -> CPUType :
#
#     C++ signature :
#         enum kdlib::CPUType getCPUType(class pykd::CPUContextAdapter {lvalue})
#
#
# 类debugEvent
# Debug evemt descriptions
#
# 基类：
# 实例
#
# 特性：
#
# 处理
# 线
# 类型
#
#
#
# 类debugOptions
# Debug options
#
# 基类：
# 枚举
#
# 值：
#
# AllowNetworkPaths：4
# DisallowNetworkPaths：8
# 初始断裂：32
# 总决赛：64
# FailIncomplete信息：512
# DisableModuleSymbolLoad：32768
# DisallowImageFileMapping：131072
# 首选Dml：262144
#
#
#
# 课堂
# din
#
# 基类：
# 实例
#
# 特性：
#
# 关闭
# 编码方式
#
#
# 方法：
#
# 阅读线
#
#
#
# 方法索引读取线
#
# readline( (din)arg1) -> str :
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > readline(class pykd::DbgIn {lvalue})
#
#
# 阶级分歧
# Class disassemble a processor instructions
#
# 基类：
# 实例
#
# 方法：
#
# __在里面__
# __str__
# 汇编
# 开始
# 当前
# 消沉
# ea
# findOffset
# 指令
# 跳
# rel子
# 长度
# 操作码
# Opmnemo
# 重启
#
#
#
# 方法disasm .__ init__
#
# __init__( (object)arg1) -> object :
#
#     C++ signature :
#         void * __ptr64 __init__(class boost::python::api::object)
#
# __init__( (object)arg1, (int)arg2) -> object :
#
#     C++ signature :
#         void * __ptr64 __init__(class boost::python::api::object,unsigned __int64)
#
#
# 方法问题。__str__
#
# __str__( (disasm)arg1) -> str :
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > __str__(class kdlib::Disasm {lvalue})
#
#
# 方法disasm.asm
#
# asm( (disasm)arg1, (str)arg2) -> str :
#     Insert assemblied instuction to current offset
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > asm(class kdlib::Disasm {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法disasm.begin
#
# begin( (disasm)arg1) -> int :
#     Return begin offset
#
#     C++ signature :
#         unsigned __int64 begin(class kdlib::Disasm {lvalue})
#
#
# 方法异议
#
# current( (disasm)arg1) -> int :
#     Return current offset
#
#     C++ signature :
#         unsigned __int64 current(class kdlib::Disasm {lvalue})
#
#
# 方法disasm.disasm
#
# disasm( (disasm)arg1) -> str :
#     Disassemble next instruction
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > disasm(class kdlib::Disasm {lvalue})
#
# disasm( (disasm)arg1, (int)arg2) -> str :
#     Disassemble from the specified offset
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > disasm(class kdlib::Disasm {lvalue},unsigned __int64)
#
#
# 方法讨论
#
# ea( (disasm)arg1) -> int :
#     Return effective address for last disassembled instruction or 0
#
#     C++ signature :
#         unsigned __int64 ea(class kdlib::Disasm {lvalue})
#
#
# 方法disasm.findOffset
#
# findOffset( (disasm)arg1, (int)arg2) -> int :
#     Return the location of a processor instruction relative to a given location
#
#     C++ signature :
#         unsigned __int64 findOffset(class kdlib::Disasm {lvalue},long)
#
#
# 方法说明
#
# instruction( (disasm)arg1) -> str :
#     Returm current disassembled instruction
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > instruction(class kdlib::Disasm {lvalue})
#
#
# 方法disasm.jump
#
# jump( (disasm)arg1, (int)arg2) -> str :
#     Change the current instruction
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > jump(class kdlib::Disasm {lvalue},unsigned __int64)
#
#
# 方法disasm.jumprel
#
# jumprel( (disasm)arg1, (int)arg2) -> str :
#     Change the current instruction
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > jumprel(class kdlib::Disasm {lvalue},long)
#
#
# 方法Disasm.length
#
# length( (disasm)arg1) -> int :
#     Return current instruction length
#
#     C++ signature :
#         unsigned __int64 length(class kdlib::Disasm {lvalue})
#
#
# 方法disasm.opcode
#
# opcode( (disasm)arg1) -> list :
#     Return list of bytes of the instruction opcode
#
#     C++ signature :
#         class boost::python::list opcode(class kdlib::Disasm {lvalue})
#
#
# 方法disasm.opmnemo
#
# opmnemo( (disasm)arg1) -> str :
#     Return mnemocode of the instruction
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > opmnemo(class kdlib::Disasm {lvalue})
#
#
# 方法重设
#
# reset( (disasm)arg1) -> str :
#     Reset current offset to begin
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > reset(class kdlib::Disasm {lvalue})
#
#
# 类斗
# dout
#
# 基类：
# 实例
#
# 特性：
#
# 关闭
# 编码方式
#
#
# 方法：
#
# 齐平
# 饱和度
# 写
# writedml
#
#
#
# 方法dout.flush
#
# flush( (dout)arg1) -> None :
#
#     C++ signature :
#         void flush(class pykd::DbgOut {lvalue})
#
#
# 方法dout.isatty
#
# isatty( (dout)arg1) -> bool :
#
#     C++ signature :
#         bool isatty(class pykd::DbgOut {lvalue})
#
#
# 方法dout.write
#
# write( (dout)arg1, (str)arg2) -> None :
#
#     C++ signature :
#         void write(class pykd::DbgOut {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法dout.writedml
#
# writedml( (dout)arg1, (str)arg2) -> None :
#
#     C++ signature :
#         void writedml(class pykd::DbgOut {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 类eventHandler
# Base class for overriding and handling debug notifications
#
# 基类：
# 实例
#
# 方法：
#
# __在里面__
# onBreakpoint
# onChangeBreakpoints
# onChangeLocalScope
# onChangeSymbolPaths
# onCurrentThreadChange
# onDebugOutput
# onException
# onExecutionStatusChange
# onLoadModule
# onStartInput
# onStopInput
# onThreadStart
# onThreadStop
# onUnloadModule
#
#
#
# 方法eventHandler .__ init__
#
# __init__( (object)arg1) -> None :
#
#     C++ signature :
#         void __init__(struct _object * __ptr64)
#
#
# 方法eventHandler.onBreakpoint
#
# onBreakpoint( (eventHandler)arg1, (int)arg2) -> eventResult :
#     Triggered breakpoint event. Parameter is int: ID of breakpoint
#     For ignore event method must return eventResult.noChange
#
#     C++ signature :
#         enum kdlib::DebugCallbackResult onBreakpoint(class pykd::EventHandler {lvalue},unsigned long)
#
#
# 方法eventHandler.onChangeBreakpoints
#
# onChangeBreakpoints( (eventHandler)arg1) -> None :
#     Breakpoints is changed for current process
#
#     C++ signature :
#         void onChangeBreakpoints(class pykd::EventHandler {lvalue})
#
#
# 方法eventHandler.onChangeLocalScope
#
# onChangeLocalScope( (eventHandler)arg1) -> None :
#     The current local scope has been changed.
#     There is no return value
#
#     C++ signature :
#         void onChangeLocalScope(class pykd::EventHandler {lvalue})
#
#
# 方法eventHandler.onChangeSymbolPaths
#
# onChangeSymbolPaths( (eventHandler)arg1) -> None :
#     Symbol paths has been changed.
#     There is no return value
#
#     C++ signature :
#         void onChangeSymbolPaths(class pykd::EventHandler {lvalue})
#
#
# 方法eventHandler.onCurrentThreadChange
#
# onCurrentThreadChange( (eventHandler)arg1, (int)arg2) -> None :
#     The current thread has been changed, which implies that the current target and current process might also have changed.
#     There is no return value
#
#     C++ signature :
#         void onCurrentThreadChange(class pykd::EventHandler {lvalue},unsigned long)
#
#
# 方法eventHandler.onDebugOutput
#
# onDebugOutput( (eventHandler)arg1, (str)arg2, (outputFlag)arg3) -> None :
#     Request debug output
#
#     C++ signature :
#         void onDebugOutput(class pykd::EventHandler {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >,enum kdlib::OutputFlag)
#
#
# 方法eventHandler.onException
#
# onException( (eventHandler)arg1, (exceptionInfo)arg2) -> eventResult :
#     Triggered exception event. Parameter - exceptionInfo
#     For ignore event method must return eventResult.noChange
#
#     C++ signature :
#         enum kdlib::DebugCallbackResult onException(class pykd::EventHandler {lvalue},struct kdlib::ExceptionInfo)
#
#
# 方法eventHandler.onExecutionStatusChange
#
# onExecutionStatusChange( (eventHandler)arg1, (executionStatus)arg2) -> None :
#     Triggered execution status changed. Parameter - execution status.
#     There is no return value
#
#     C++ signature :
#         void onExecutionStatusChange(class pykd::EventHandler {lvalue},enum kdlib::ExecutionStatus)
#
#
# 方法eventHandler.onLoadModule
#
# onLoadModule( (eventHandler)arg1, (int)arg2, (str)arg3) -> eventResult :
#     Triggered module load event. Parameter are long: module base, string: module name
#     For ignore event method must return eventResult.noChange
#
#     C++ signature :
#         enum kdlib::DebugCallbackResult onLoadModule(class pykd::EventHandler {lvalue},unsigned __int64,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法eventHandler.onStartInput
#
# onStartInput( (eventHandler)arg1) -> None :
#     Request debug input
#
#     C++ signature :
#         void onStartInput(class pykd::EventHandler {lvalue})
#
#
# 方法eventHandler.onStopInput
#
# onStopInput( (eventHandler)arg1) -> None :
#     Debug input is completed
#
#     C++ signature :
#         void onStopInput(class pykd::EventHandler {lvalue})
#
#
# 方法eventHandler.onThreadStart
#
# onThreadStart( (eventHandler)arg1) -> eventResult :
#     New thread is started in the current process
#
#     C++ signature :
#         enum kdlib::DebugCallbackResult onThreadStart(class pykd::EventHandler {lvalue})
#
#
# 方法eventHandler.onThreadStop
#
# onThreadStop( (eventHandler)arg1) -> eventResult :
#     A thread is stopped in the current thread
#
#     C++ signature :
#         enum kdlib::DebugCallbackResult onThreadStop(class pykd::EventHandler {lvalue})
#
#
# 方法eventHandler.onUnloadModule
#
# onUnloadModule( (eventHandler)arg1, (int)arg2, (str)arg3) -> eventResult :
#     Triggered module unload event. Parameter are  long: module base, string: module name
#     For ignore event method must return eventResult.noChange
#
#     C++ signature :
#         enum kdlib::DebugCallbackResult onUnloadModule(class pykd::EventHandler {lvalue},unsigned __int64,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 类eventResult
# Return value of event handler
#
# 基类：
# 枚举
#
# 值：
#
# 进行：0
# NoChange：1
# 休息：2
#
#
#
# 类eventType
# Type of debug event
#
# 基类：
# 枚举
#
# 值：
#
# 断点：1
# 例外：2
# CreateThread：3
# ExitThread：4
# CreateProcess：5
# ExitProcess：6
# 加载模块数：7
# 卸载模块数：8
# 系统错误：9
# SessionStatus：10
# ChangeDebuggeeState：11
# ChangeEngineState：12
# ChangeSymbolState：13
#
#
#
# 类exceptionInfo
# Exception information
#
# 基类：
# 实例
#
# 特性：
#
# exceptionAddress
# exceptionCode
# exceptionFlags
# exceptionRecord
# firstChance
# 参数
#
#
# 方法：
#
# __str__
#
#
#
# 属性exceptionInfo.exceptionAddress
# The address where the exception occurred
#
#
# 属性exceptionInfo.exceptionCode
# The reason the exception occurred
#
#
# 属性exceptionInfo.exceptionFlags
# The exception flags
#
#
# 属性exceptionInfo.exceptionRecord
# A pointer to an associated EXCEPTION_RECORD structure
#
#
# 属性exceptionInfo.firstChance
# Specifies whether this exception has been previously encountered
#
#
# 属性exceptionInfo.parameters
# An array of additional arguments that describe the exception
#
#
# 方法exceptionInfo .__ str__
#
# __str__( (exceptionInfo)arg1) -> str :
#     Return object as a string
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > __str__(struct kdlib::ExceptionInfo {lvalue})
#
#
# 类执行状态
# Execution Status
#
# 基类：
# 枚举
#
# 值：
#
# 无更改：0
# 前进：1
# 休息：2
# NoDebuggee：3
#
#
#
# 类memoryProtect
# Memory protection attribiuties
#
# 基类：
# 枚举
#
# 值：
#
# PageNoAccess：1
# PageReadOnly：2
# PageReadWrite：4
# PageWriteCopy：2
# PageExecute：16
# PageExecuteRead：32
# PageExecuteReadWrite：64
# PageExecuteWriteCopy：128
#
#
#
# 类模块
# Class representing executable module
#
# 基类：
# numVariant
#
# 方法：
#
# __包含__
# __getattr__
# __getitem__
# __在里面__
# __str__
# 开始
# 校验和
# containsRecord
# 结束
# 枚举符号
# 枚举类型
# findSymbol
# findSymbolAndDisp
# getFixedFileInfo
# getVersion
# hasSymbol
# 图片
# 名称
# 抵销
# queryVersion
# 重装
# RVA
# 尺寸
# 大小
# 符号文件
# 时间戳记
# 类型
# 类型Var
# typedVarArray
# typedVarList
# 嗯
# 卸载
#
#
#
# 方法模块。__包含__
#
# __contains__( (module)arg1, (str)arg2) -> bool :
#
#     C++ signature :
#         bool __contains__(class boost::shared_ptr<class kdlib::Module> {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法模块.__ getattr__
#
# __getattr__( (module)arg1, (str)arg2) -> object :
#     Return symbol offset or type as attribute
#
#     C++ signature :
#         class boost::python::api::object __getattr__(class kdlib::Module {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法模块.__ getitem__
#
# __getitem__( (module)arg1, (str)arg2) -> object :
#     Return symbol offset or type as item
#
#     C++ signature :
#         class boost::python::api::object __getitem__(class kdlib::Module {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法模块.__ init__
#
# __init__( (object)arg1, (str)arg2) -> object :
#
#     C++ signature :
#         void * __ptr64 __init__(class boost::python::api::object,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
# __init__( (object)arg1, (int)arg2) -> object :
#
#     C++ signature :
#         void * __ptr64 __init__(class boost::python::api::object,unsigned __int64)
#
#
# 方法模块。__str__
#
# __str__( (module)arg1) -> str :
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > __str__(class kdlib::Module {lvalue})
#
#
# 方法module.begin
#
# begin( (module)arg1) -> int :
#     Return start address of the module
#
#     C++ signature :
#         unsigned __int64 begin(class kdlib::Module {lvalue})
#
#
# 方法模块。校验和
#
# checksum( (module)arg1) -> int :
#     Return a image file checksum: IMAGE_OPTIONAL_HEADER.CheckSum
#
#     C++ signature :
#         unsigned long checksum(class kdlib::Module {lvalue})
#
#
# 方法模块。
#
# containingRecord( (module)arg1, (int)arg2, (str)arg3, (str)arg4) -> typedVar :
#     Return instance of the typedVar class. It's value are loaded from the target memory.The start address is calculated by the same method as the standard macro CONTAINING_RECORD does
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> containingRecord(class kdlib::Module {lvalue},unsigned __int64,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法模块
#
# end( (module)arg1) -> int :
#     Return end address of the module
#
#     C++ signature :
#         unsigned __int64 end(class kdlib::Module {lvalue})
#
#
# 方法module.enumSymbols
#
# enumSymbols( (module)arg1 [, (str)mask]) -> list :
#     Return list of tuple ( symbolname, offset )
#
#     C++ signature :
#         class boost::python::list enumSymbols(class kdlib::Module {lvalue} [,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >])
#
#
# 方法module.enumTypes
#
# enumTypes( (module)arg1 [, (str)mask]) -> list :
#     Return list of types name
#
#     C++ signature :
#         class boost::python::list enumTypes(class kdlib::Module {lvalue} [,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >])
#
#
# 方法module.findSymbol
#
# findSymbol( (module)arg1, (int)offset [, (bool)showDisplacement]) -> str :
#     Return symbol name by virtual address
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > findSymbol(class kdlib::Module {lvalue},unsigned __int64 [,bool])
#
#
# 方法module.findSymbolAndDisp
#
# findSymbolAndDisp( (module)arg1, (int)arg2) -> tuple :
#     Return tuple(symbol_name, displacement) by virtual address
#
#     C++ signature :
#         class boost::python::tuple findSymbolAndDisp(class kdlib::Module {lvalue},unsigned __int64)
#
#
# 方法module.getFixedFileInfo
#
# getFixedFileInfo( (module)arg1) -> FixedFileInfo :
#     Return FixedFileInfo
#
#     C++ signature :
#         class boost::shared_ptr<struct kdlib::FixedFileInfo> getFixedFileInfo(class kdlib::Module {lvalue})
#
#
# 方法module.getVersion
#
# getVersion( (module)arg1) -> tuple :
#     Return tuple of the module's file version
#
#     C++ signature :
#         class boost::python::tuple getVersion(class kdlib::Module {lvalue})
#
#
# 方法module.hasSymbol
#
# hasSymbol( (module)arg1, (str)arg2) -> bool :
#     Check if a module has the specified symbol
#
#     C++ signature :
#         bool hasSymbol(class boost::shared_ptr<class kdlib::Module> {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法模块图像
#
# image( (module)arg1) -> str :
#     Return name of the image of the module
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > image(class kdlib::Module {lvalue})
#
#
# 方法module.name
#
# name( (module)arg1) -> str :
#     Return name of the module
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > name(class kdlib::Module {lvalue})
#
#
# 方法module.offset
#
# offset( (module)arg1, (str)arg2) -> int :
#     Return offset of the symbol
#
#     C++ signature :
#         unsigned __int64 offset(class kdlib::Module {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法module.queryVersion
#
# queryVersion( (module)arg1, (str)arg2) -> str :
#     Return string from the module's version resources
#
#     C++ signature :
#         class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > queryVersion(class kdlib::Module {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
#
#
# 方法module.reload
#
# reload( (module)arg1) -> None :
#     (Re)load symbols for the module
#
#     C++ signature :
#         void reload(class kdlib::Module {lvalue})
#
#
# 方法module.rva
#
# rva( (module)arg1, (str)arg2) -> int :
#     Return rva of the symbol
#
#     C++ signature :
#         unsigned long rva(class kdlib::Module {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法module.size
#
# size( (module)arg1) -> int :
#     Return size of the module
#
#     C++ signature :
#         unsigned __int64 size(class kdlib::Module {lvalue})
#
#
# 方法module.sizeof
#
# sizeof( (module)arg1, (str)arg2) -> int :
#     Return a size of the type or variable
#
#     C++ signature :
#         unsigned __int64 sizeof(class kdlib::Module {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法module.symfile
#
# symfile( (module)arg1) -> str :
#     Return the full path to the module's symbol information
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > symfile(class kdlib::Module {lvalue})
#
#
# 方法module.timestamp
#
# timestamp( (module)arg1) -> int :
#     Return a low 32 bits of the time stamp of the image: IMAGE_FILE_HEADER.TimeDateStamp
#
#     C++ signature :
#         unsigned long timestamp(class kdlib::Module {lvalue})
#
#
# 方法模块类型
#
# type( (module)arg1, (str)arg2) -> typeInfo :
#     Return typeInfo class by type name
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> type(class kdlib::Module {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法module.typedVar
#
# typedVar( (module)arg1, (int)arg2) -> typedVar :
#     Return a typedVar class instance
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> typedVar(class kdlib::Module {lvalue},unsigned __int64)
#
# typedVar( (module)arg1, (str)arg2) -> typedVar :
#     Return a typedVar class instance
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> typedVar(class kdlib::Module {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
# typedVar( (module)arg1, (str)arg2, (object)arg3) -> typedVar :
#     Return a typedVar class instance
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> typedVar(class kdlib::Module {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >,class boost::python::api::object {lvalue})
#
# typedVar( (module)arg1, (str)arg2, (str)arg3) -> typedVar :
#     Return a typedVar class instance
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> typedVar(class kdlib::Module {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法module.typedVarArray
#
# typedVarArray( (module)arg1, (int)arg2, (str)arg3, (int)arg4) -> list :
#     Return a list of the typedVar class instances. Each item represents an item of the counted array in the target memory
#
#     C++ signature :
#         class boost::python::list typedVarArray(class kdlib::Module {lvalue},unsigned __int64,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >,unsigned __int64)
#
#
# 方法module.typedVarList
#
# typedVarList( (module)arg1, (int)arg2, (str)arg3, (str)arg4) -> list :
#     Return a list of the typedVar class instances. Each item represents an item of the linked list in the target memory
#
#     C++ signature :
#         class boost::python::list typedVarList(class kdlib::Module {lvalue},unsigned __int64,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法模块
#
# um( (module)arg1) -> bool :
#     Returns a flag that the module is a user-mode module
#
#     C++ signature :
#         bool um(class kdlib::Module {lvalue})
#
#
# 方法module.unloaded
#
# unloaded( (module)arg1) -> bool :
#     Returns a flag that the module was unloaded
#
#     C++ signature :
#         bool unloaded(class kdlib::Module {lvalue})
#
#
# numVariant类
# numVariant
#
# 基类：
# 实例
#
# 方法：
#
# __加__
# __和__
# __eq__
# __浮动__
# __floordiv__
# __ge__
# __gt__
# __哈希__
# __hex__
# __指数__
# __int__
# __倒置__
# __le__
# __长__
# __lshift__
# __lt__
# __mod__
# __mul__
# __ne__
# __否__
# __nonzero__
# __要么__
# __pos__
# __radd__
# __rand__
# __rfloordiv__
# __rlshift__
# __rmod__
# __rmul__
# ______
# __rrshift__
# __rshift__
# __rsub__
# __rtruediv__
# __rxor__
# __str__
# __sub__
# __truediv__
# __xor__
# isInteger
#
#
#
# 方法numVariant .__ add__
#
# __add__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __add__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__和__
#
# __and__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __and__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ eq__
#
# __eq__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __eq__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ float__
#
# __float__( (numVariant)arg1) -> object :
#
#     C++ signature :
#         class boost::python::api::object __float__(class kdlib::NumConvertable {lvalue})
#
#
# 方法numVariant .__ floordiv__
#
# __floordiv__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __floordiv__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ ge__
#
# __ge__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __ge__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ gt__
#
# __gt__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __gt__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ hash__
#
# __hash__( (numVariant)arg1) -> object :
#
#     C++ signature :
#         class boost::python::api::object __hash__(class kdlib::NumConvertable {lvalue})
#
#
# 方法numVariant .__ hex__
#
# __hex__( (numVariant)arg1) -> str :
#
#     C++ signature :
#         class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > __hex__(class kdlib::NumConvertable {lvalue})
#
#
# 方法numVariant .__ index__
#
# __index__( (numVariant)arg1) -> object :
#
#     C++ signature :
#         class boost::python::api::object __index__(class kdlib::NumConvertable {lvalue})
#
#
# 方法numVariant .__ int__
#
# __int__( (numVariant)arg1) -> object :
#
#     C++ signature :
#         class boost::python::api::object __int__(class kdlib::NumConvertable {lvalue})
#
#
# 方法numVariant .__ invert__
#
# __invert__( (numVariant)arg1) -> object :
#
#     C++ signature :
#         class boost::python::api::object __invert__(class kdlib::NumConvertable {lvalue})
#
#
# 方法numVariant .__ le__
#
# __le__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __le__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ long__
#
# __long__( (numVariant)arg1) -> object :
#
#     C++ signature :
#         class boost::python::api::object __long__(class kdlib::NumConvertable {lvalue})
#
#
# 方法numVariant .__ lshift__
#
# __lshift__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __lshift__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ lt__
#
# __lt__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __lt__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ mod__
#
# __mod__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __mod__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ mul__
#
# __mul__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __mul__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ ne__
#
# __ne__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __ne__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ neg__
#
# __neg__( (numVariant)arg1) -> object :
#
#     C++ signature :
#         class boost::python::api::object __neg__(class kdlib::NumConvertable {lvalue})
#
#
# 方法numVariant .__ nonzero__
#
# __nonzero__( (numVariant)arg1) -> object :
#
#     C++ signature :
#         class boost::python::api::object __nonzero__(class kdlib::NumConvertable {lvalue})
#
#
# 方法numVariant .__ or__
#
# __or__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __or__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ pos__
#
# __pos__( (numVariant)arg1) -> object :
#
#     C++ signature :
#         class boost::python::api::object __pos__(class kdlib::NumConvertable {lvalue})
#
#
# 方法numVariant .__ radd__
#
# __radd__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __radd__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ rand__
#
# __rand__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __rand__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ rfloordiv__
#
# __rfloordiv__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __rfloordiv__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ rlshift__
#
# __rlshift__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __rlshift__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ rmod__
#
# __rmod__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __rmod__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ rmul__
#
# __rmul__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __rmul__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ ror__
#
# __ror__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __ror__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ rrshift__
#
# __rrshift__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __rrshift__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ rshift__
#
# __rshift__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __rshift__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ rsub__
#
# __rsub__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __rsub__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ rtruediv__
#
# __rtruediv__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __rtruediv__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ rxor__
#
# __rxor__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __rxor__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ str__
#
# __str__( (numVariant)arg1) -> str :
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > __str__(class kdlib::NumConvertable {lvalue})
#
#
# 方法numVariant .__ sub__
#
# __sub__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __sub__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ truediv__
#
# __truediv__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __truediv__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant .__ xor__
#
# __xor__( (numVariant)arg1, (object)arg2) -> object :
#
#     C++ signature :
#         class boost::python::api::object __xor__(class kdlib::NumConvertable {lvalue},class boost::python::api::object {lvalue})
#
#
# 方法numVariant.isInteger
#
# isInteger( (numVariant)arg1) -> bool :
#
#     C++ signature :
#         bool isInteger(class kdlib::NumConvertable {lvalue})
#
#
# 类outputFlag
# Set of output mask
#
# 基类：
# 枚举
#
# 值：
#
# 正常：1
# 错误：2
# 警告：4
# 详细：8
# 提示：16
# 提示注册：32
# 扩展警告：64
# 调试对象：128
# 侦错提示：256
# 符号：512
# 状态：1024
# 全部：2047
#
#
#
# 类stackFrame
# class for stack's frame representation
#
# 基类：
# 实例
#
# 特性：
#
# fp
# frameOffset
# structionOffset
# ip
# 当地人
# 参数
# 退回
# returnOffset
# SP
# stackOffset
#
#
# 方法：
#
# __str__
# findSymbol
# getLocal
# getLocals
# getParam
# getParams
# getSourceLine
# isInline
# 切换到
#
#
#
# 属性stackFrame.fp
# frame pointer
#
#
# 属性stackFrame.frameOffset
# Return a frame's offset
#
#
# 属性stackFrame.instructionOffset
# Return a frame's instruction offset
#
#
# 属性stackFrame.ip
# instruction pointer
#
#
# 属性stackFrame.locals
# return a set of  function's local variables as a dict ( name : value)
#
#
# 属性stackFrame.params
# return set of function's parameters as a dict (name : value)
#
#
# 属性stackFrame.ret
# return pointer
#
#
# 属性stackFrame.returnOffset
# Return a frame's return offset
#
#
# 属性stackFrame.sp
# stack pointer
#
#
# 属性stackFrame.stackOffset
# Return a frame's stack offset
#
#
# 方法stackFrame .__ str__
#
# __str__( (stackFrame)arg1) -> str :
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > __str__(class boost::shared_ptr<class kdlib::StackFrame> {lvalue})
#
#
# 方法stackFrame.findSymbol
#
# findSymbol( (stackFrame)arg1) -> tuple :
#     return symbol for frame's instruction pointer
#
#     C++ signature :
#         class boost::python::tuple findSymbol(class boost::shared_ptr<class kdlib::StackFrame> {lvalue})
#
#
# 方法stackFrame.getLocal
#
# getLocal( (stackFrame)arg1, (str)arg2) -> typedVar :
#     return the function's local variable  by it's name
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> getLocal(class boost::shared_ptr<class kdlib::StackFrame> {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法stackFrame.getLocals
#
# getLocals( (stackFrame)arg1) -> list :
#     return set of function's local variables  as a  list of tuple (name, value )
#
#     C++ signature :
#         class boost::python::list getLocals(class boost::shared_ptr<class kdlib::StackFrame> {lvalue})
#
#
# 方法stackFrame.getParam
#
# getParam( (stackFrame)arg1, (str)arg2) -> typedVar :
#     return function param by it's name
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> getParam(class boost::shared_ptr<class kdlib::StackFrame> {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法stackFrame.getParams
#
# getParams( (stackFrame)arg1) -> list :
#     return set of function's parameters  as a  list of tuple (name, value )
#
#     C++ signature :
#         class boost::python::list getParams(class boost::shared_ptr<class kdlib::StackFrame> {lvalue})
#
#
# 方法stackFrame.getSourceLine
#
# getSourceLine( (stackFrame)arg1) -> tuple :
#     return source line for stack frame's function
#
#     C++ signature :
#         class boost::python::tuple getSourceLine(class boost::shared_ptr<class kdlib::StackFrame> {lvalue})
#
#
# 方法stackFrame.isInline
#
# isInline( (stackFrame)arg1) -> bool :
#     this virtual frame of inlined function
#
#     C++ signature :
#         bool isInline(class boost::shared_ptr<class kdlib::StackFrame> {lvalue})
#
#
# 方法stackFrame.switchTo
#
# switchTo( (stackFrame)arg1) -> None :
#     Make this frame a current
#
#     C++ signature :
#         void switchTo(class boost::shared_ptr<class kdlib::StackFrame> {lvalue})
#
#
# 类symbolIterator
# Iterator for symbols
#
# 基类：
# 实例
#
# 方法：
#
# __iter__
# __下一个__
#
#
#
# 方法symbolIterator .__ iter__
#
# __iter__( (object)arg1) -> object :
#
#     C++ signature :
#         class boost::python::api::object __iter__(class boost::python::api::object)
#
#
# 方法symbolIterator .__ next__
#
# __next__( (symbolIterator)arg1) -> tuple :
#
#     C++ signature :
#         class boost::python::tuple __next__(struct pykd::SymbolEnumeratorAdapter {lvalue})
#
#
# 类symbolProvider
# Get abstaract access to different type info sources
#
# 基类：
# 实例
#
# 方法：
#
# __iter__
# 重复
#
#
#
# 方法symbolProvider .__ iter__
#
# __iter__( (symbolProvider)arg1) -> symbolIterator :
#
#     C++ signature :
#         struct pykd::SymbolEnumeratorAdapter * __ptr64 __iter__(class boost::shared_ptr<class kdlib::SymbolProvider>)
#
#
# 方法symbolProvider.iter
#
# iter( (symbolProvider)arg1, (str)arg2) -> symbolIterator :
#     Return type iterator with specified mask
#
#     C++ signature :
#         struct pykd::SymbolEnumeratorAdapter * __ptr64 iter(class boost::shared_ptr<class kdlib::SymbolProvider>,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 类类Symbol
# Structure describes a synthetic symbol within a module
#
# 基类：
# 实例
#
# 特性：
#
# moduleBase
# symbolId
#
#
# 方法：
#
# __str__
#
#
#
# 属性syntheticSymbol.moduleBase
# The location in the target's virtual address space of the module's base address
#
#
# 属性syntheticSymbol.symbolId
# The symbol ID of the symbol within the module
#
#
# 方法CompositeSymbol .__ str__
#
# __str__( (syntheticSymbol)arg1) -> str :
#     Return object as a string
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > __str__(struct kdlib::SyntheticSymbol)
#
#
# 类systemVersion
# Operation system version
#
# 基类：
# 实例
#
# 特性：
#
# buildNumber
# buildString
# 服务包
# win32Major
# win32Minor
#
#
# 方法：
#
# __str__
#
#
#
# 属性systemVersion.buildNumber
# Build number for the target's operating system
#
#
# 属性systemVersion.buildString
# String that identifies the build of the system
#
#
# 属性systemVersion.servicePack
# Service Pack Number
#
#
# 属性系统Version.win32Major
# Major version number of the target's operating system
#
#
# 属性系统Version.win32Minor
# Minor version number of the target's operating system
#
#
# 方法systemVersion .__ str__
#
# __str__( (systemVersion)arg1) -> str :
#     Return object as a string
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > __str__(struct kdlib::SystemInfo {lvalue})
#
#
# 类目标堆
# Class representing heap in the target process
#
# 基类：
# 实例
#
# 方法：
#
# 参赛作品
#
#
#
# 方法targetHeap.entries
#
# entries( (targetHeap)arg1 [, (str)typeName [, (int)minSize [, (int)maxSize]]]) -> targetHeapIterator :
#     Return heap's entries iterator object
#
#     C++ signature :
#         class pykd::TargetHeapIterator * __ptr64 entries(class kdlib::TargetHeap {lvalue} [,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > [,unsigned __int64 [,unsigned __int64]]])
#
#
# 类targetHeapIterator
# iterator for typedVar array
#
# 基类：
# 实例
#
# 方法：
#
# __iter__
# __len__
# __下一个__
#
#
#
# 方法targetHeapIterator .__ iter__
#
# __iter__( (object)arg1) -> object :
#
#     C++ signature :
#         class boost::python::api::object __iter__(class boost::python::api::object)
#
#
# 方法targetHeapIterator .__ len__
#
# __len__( (targetHeapIterator)arg1) -> int :
#
#     C++ signature :
#         unsigned __int64 __len__(class pykd::TargetHeapIterator {lvalue})
#
#
# 方法targetHeapIterator .__ next__
#
# __next__( (targetHeapIterator)arg1) -> tuple :
#
#     C++ signature :
#         class boost::python::tuple __next__(class pykd::TargetHeapIterator {lvalue})
#
#
# 类targetProcess
# Class representing process in the target system
#
# 基类：
# 实例
#
# 特性：
#
# exe名称
# ID
# eb
# 系统ID
#
#
# 方法：
#
# __在里面__
# __str__
# 断点
# currentThread
# getBreakpoint
# getManagedHeap
# getManagedVar
# getModule
# getModuleByName
# getModuleByOffset
# getNumberBreakpoints
# getNumberModules
# getNumberThreads
# getThread
# getThreadById
# getThreadBySystemId
# isCurrent
# 被管理
# 模组
# 设定电流
# 线程数
#
#
#
# 属性targetProcess.exeName
# Return the process executable file name
#
#
# 属性targetProcess.id
# Return process id
#
#
# 属性targetProcess.peb
# Return PEB address
#
#
# 属性targetProcess.systemID
# Retrun system process ID ( PID )
#
#
# 方法targetProcess .__ init__
#
# __init__( (object)arg1 [, (int)arg2]) -> object :
#
#     C++ signature :
#         void * __ptr64 __init__(class boost::python::api::object [,unsigned long])
#
#
# 方法targetProcess .__ str__
#
# __str__( (targetProcess)arg1) -> str :
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > __str__(class kdlib::TargetProcess {lvalue})
#
#
# 方法targetProcess.breakpoints
#
# breakpoints( (targetProcess)arg1) -> list :
#     Return list of breakpoints for the target process
#
#     C++ signature :
#         class boost::python::list breakpoints(class kdlib::TargetProcess {lvalue})
#
#
# 方法targetProcess.currentThread
#
# currentThread( (targetProcess)arg1) -> targetThread :
#     Return current thread
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TargetThread> currentThread(class kdlib::TargetProcess {lvalue})
#
#
# 方法targetProcess.getBreakpoint
#
# getBreakpoint( (targetProcess)arg1, (int)arg2) -> breakpoint :
#     Return a breakpoint by it's index
#
#     C++ signature :
#         class pykd::Breakpoint * __ptr64 getBreakpoint(class kdlib::TargetProcess {lvalue},unsigned long)
#
#
# 方法targetProcess.getManagedHeap
#
# getManagedHeap( (targetProcess)arg1) -> targetHeap :
#     Return object representing a managed heap
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TargetHeap> getManagedHeap(class kdlib::TargetProcess {lvalue})
#
#
# 方法targetProcess.getManagedVar
#
# getManagedVar( (targetProcess)arg1, (int)arg2) -> typedVar :
#     Return object representing a managed object in the target managed process
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> getManagedVar(class kdlib::TargetProcess {lvalue},unsigned __int64)
#
#
# 方法targetProcess.getModule
#
# getModule( (targetProcess)arg1, (int)arg2) -> module :
#     Return a module object by it's index
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::Module> getModule(class kdlib::TargetProcess {lvalue},unsigned long)
#
#
# 方法targetProcess.getModuleByName
#
# getModuleByName( (targetProcess)arg1, (str)arg2) -> module :
#     Return a module object by it's name
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::Module> getModuleByName(class kdlib::TargetProcess {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法targetProcess.getModuleByOffset
#
# getModuleByOffset( (targetProcess)arg1, (int)arg2) -> module :
#     Return a module object by it's offset
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::Module> getModuleByOffset(class kdlib::TargetProcess {lvalue},unsigned __int64)
#
#
# 方法targetProcess.getNumberBreakpoints
#
# getNumberBreakpoints( (targetProcess)arg1) -> int :
#     Return number of breakpoints for this process
#
#     C++ signature :
#         unsigned long getNumberBreakpoints(class kdlib::TargetProcess {lvalue})
#
#
# 方法targetProcess.getNumberModules
#
# getNumberModules( (targetProcess)arg1) -> int :
#     Return number of modules for this process
#
#     C++ signature :
#         unsigned long getNumberModules(class kdlib::TargetProcess {lvalue})
#
#
# 方法targetProcess.getNumberThreads
#
# getNumberThreads( (targetProcess)arg1) -> int :
#     Return number of threads for this process
#
#     C++ signature :
#         unsigned long getNumberThreads(class kdlib::TargetProcess {lvalue})
#
#
# 方法targetProcess.getThread
#
# getThread( (targetProcess)arg1, (int)arg2) -> targetThread :
#     Return thread by its index
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TargetThread> getThread(class kdlib::TargetProcess {lvalue},unsigned long)
#
#
# 方法targetProcess.getThreadById
#
# getThreadById( (targetProcess)arg1, (int)arg2) -> targetThread :
#     Return thread by its index
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TargetThread> getThreadById(class kdlib::TargetProcess {lvalue},unsigned long)
#
#
# 方法targetProcess.getThreadBySystemId
#
# getThreadBySystemId( (targetProcess)arg1, (int)arg2) -> targetThread :
#     Return thread by tid
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TargetThread> getThreadBySystemId(class kdlib::TargetProcess {lvalue},unsigned long)
#
#
# 方法targetProcess.isCurrent
#
# isCurrent( (targetProcess)arg1) -> bool :
#     Check if the target is current
#
#     C++ signature :
#         bool isCurrent(class kdlib::TargetProcess {lvalue})
#
#
# 方法targetProcess.isManaged
#
# isManaged( (targetProcess)arg1) -> bool :
#     Check if the taget process is managed
#
#     C++ signature :
#         bool isManaged(class kdlib::TargetProcess {lvalue})
#
#
# 方法targetProcess.modules
#
# modules( (targetProcess)arg1) -> list :
#     Return list of modules for the target process
#
#     C++ signature :
#         class boost::python::list modules(class kdlib::TargetProcess {lvalue})
#
#
# 方法targetProcess.setCurrent
#
# setCurrent( (targetProcess)arg1) -> None :
#     Set this process as a current
#
#     C++ signature :
#         void setCurrent(class kdlib::TargetProcess {lvalue})
#
#
# 方法targetProcess.threads
#
# threads( (targetProcess)arg1) -> list :
#     Return list of threads for the target process
#
#     C++ signature :
#         class boost::python::list threads(class kdlib::TargetProcess {lvalue})
#
#
# 类targetSystem
# Class representing target system
#
# 基类：
# 实例
#
# 特性：
#
# 描述
# ID
#
#
# 方法：
#
# __在里面__
# __str__
# currentProcess
# getNumberProcesses
# getProcess
# getProcessById
# getProcessBySystemId
# is64bit系统
# isCurrent
# isDumpAnalyzing
# isKernelDebugging
# 流程
# 设定电流
#
#
#
# 属性targetSystem.desc
# Retunr target system description
#
#
# 属性targetSystem.id
# Return id of the target system
#
#
# 方法targetSystem .__ init__
#
# __init__( (object)arg1) -> object :
#
#     C++ signature :
#         void * __ptr64 __init__(class boost::python::api::object)
#
# __init__( (object)arg1, (int)arg2) -> object :
#
#     C++ signature :
#         void * __ptr64 __init__(class boost::python::api::object,unsigned long)
#
#
# 方法targetSystem .__ str__
#
# __str__( (targetSystem)arg1) -> str :
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > __str__(class kdlib::TargetSystem {lvalue})
#
#
# 方法targetSystem.currentProcess
#
# currentProcess( (targetSystem)arg1) -> targetProcess :
#     Return current process
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TargetProcess> currentProcess(class kdlib::TargetSystem {lvalue})
#
#
# 方法targetSystem.getNumberProcesses
#
# getNumberProcesses( (targetSystem)arg1) -> int :
#     Return processed number of the target system
#
#     C++ signature :
#         unsigned long getNumberProcesses(class kdlib::TargetSystem {lvalue})
#
#
# 方法targetSystem.getProcess
#
# getProcess( (targetSystem)arg1, (int)arg2) -> targetProcess :
#     Return process by index
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TargetProcess> getProcess(class kdlib::TargetSystem {lvalue},unsigned long)
#
#
# 方法targetSystem.getProcessById
#
# getProcessById( (targetSystem)arg1, (int)arg2) -> targetProcess :
#     Return process by id
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TargetProcess> getProcessById(class kdlib::TargetSystem {lvalue},unsigned long)
#
#
# 方法targetSystem.getProcessBySystemId
#
# getProcessBySystemId( (targetSystem)arg1, (int)arg2) -> targetProcess :
#     Return process by PID
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TargetProcess> getProcessBySystemId(class kdlib::TargetSystem {lvalue},unsigned long)
#
#
# 方法targetSystem.is64bitSystem
#
# is64bitSystem( (targetSystem)arg1) -> bool :
#     Check if 64 bit system running
#
#     C++ signature :
#         bool is64bitSystem(class kdlib::TargetSystem {lvalue})
#
#
# 方法targetSystem.isCurrent
#
# isCurrent( (targetSystem)arg1) -> bool :
#     Check if the target is current
#
#     C++ signature :
#         bool isCurrent(class kdlib::TargetSystem {lvalue})
#
#
# 方法targetSystem.isDumpAnalyzing
#
# isDumpAnalyzing( (targetSystem)arg1) -> bool :
#     Check if it is a dump analyzing ( not living debuggee )
#
#     C++ signature :
#         bool isDumpAnalyzing(class kdlib::TargetSystem {lvalue})
#
#
# 方法targetSystem.isKernelDebugging
#
# isKernelDebugging( (targetSystem)arg1) -> bool :
#     Check if kernel dubugging is running
#
#     C++ signature :
#         bool isKernelDebugging(class kdlib::TargetSystem {lvalue})
#
#
# 方法targetSystem.processes
#
# processes( (targetSystem)arg1) -> list :
#     get list of processes for the target system
#
#     C++ signature :
#         class boost::python::list processes(class kdlib::TargetSystem {lvalue})
#
#
# 方法targetSystem.setCurrent
#
# setCurrent( (targetSystem)arg1) -> None :
#     set system as a current
#
#     C++ signature :
#         void setCurrent(class kdlib::TargetSystem {lvalue})
#
#
# 类targetThread
# Class representing thread in the target process
#
# 基类：
# 实例
#
# 特性：
#
# fp
# frameOffset
# ID
# structionOffset
# ip
# SP
# stackOffset
# 系统ID
# teb
#
#
# 方法：
#
# __在里面__
# __str__
# isCurrent
# 设定电流
# 堆
#
#
#
# 属性targetThread.fp
# frame pointer
#
#
# 属性targetThread.frameOffset
# Return a frame's offset
#
#
# 属性targetThread.id
# Return thread's id
#
#
# 属性targetThread.instructionOffset
# Return an instruction offset
#
#
# 属性targetThread.ip
# instruction pointer
#
#
# 属性targetThread.sp
# stack pointer
#
#
# 属性targetThread.stackOffset
# Return a stack pointer
#
#
# 属性targetThread.systemID
# Retrun system thread ID ( TID )
#
#
# 属性targetThread.teb
# Return TEB address
#
#
# 方法targetThread .__ init__
#
# __init__( (object)arg1 [, (int)arg2]) -> object :
#
#     C++ signature :
#         void * __ptr64 __init__(class boost::python::api::object [,unsigned long])
#
#
# 方法targetThread .__ str__
#
# __str__( (targetThread)arg1) -> str :
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > __str__(class kdlib::TargetThread {lvalue})
#
#
# 方法targetThread.isCurrent
#
# isCurrent( (targetThread)arg1) -> bool :
#     Check if this thread is current
#
#     C++ signature :
#         bool isCurrent(class kdlib::TargetThread {lvalue})
#
#
# 方法targetThread.setCurrent
#
# setCurrent( (targetThread)arg1) -> None :
#     Set this thread current
#
#     C++ signature :
#         void setCurrent(class kdlib::TargetThread {lvalue})
#
#
# 方法targetThread.stack
#
# stack( (targetThread)arg1) -> list :
#     Get thread's stack tarce
#
#     C++ signature :
#         class boost::python::list stack(class kdlib::TargetThread {lvalue})
#
#
# 类typeInfo
# Class representing typeInfo
#
# 基类：
# numVariant
#
# 方法：
#
# __布尔__
# __包含__
# __dir__
# __getattr__
# __getitem__
# __在里面__
# __len__
# __str__
# 附加
# arrayOf
# baseClass
# baseClassOffset
# baseClasses
# bitOffset
# 位宽
# 取消引用
# 领域
# fieldName
# fieldOffset
# 领域
# getCallingConvention
# getClassParent
# getNumberBaseClasses
# getNumberFields
# getNumberMethods
# getTemplateArgs
# getTypedVar
# hasField
# hasMethod
# isArray
# isBase
# isBitField
# isConstField
# isConstant
# isEnum
# isFunction
# isNoType
# isPointer
# isStaticField
# isTemplate
# isUserDefined
# isVoid
# isVtbl
# 成员
# 方法
# methodName
# 名称
# ptrTo
# scopeName
# 尺寸
# staticOffset
#
#
#
# 方法typeInfo .__ bool__
#
# __bool__( (typeInfo)arg1) -> bool :
#
#     C++ signature :
#         bool __bool__(class kdlib::TypeInfo {lvalue})
#
#
# 方法类型Info .__包含__
#
# __contains__( (typeInfo)arg1, (str)arg2) -> bool :
#
#     C++ signature :
#         bool __contains__(class boost::shared_ptr<class kdlib::TypeInfo> {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法类型Info .__ dir__
#
# __dir__( (typeInfo)arg1) -> list :
#
#     C++ signature :
#         class boost::python::list __dir__(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo .__ getattr__
#
# __getattr__( (typeInfo)arg1, (str)arg2) -> typeInfo :
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> __getattr__(class kdlib::TypeInfo {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法typeInfo .__ getitem__
#
# __getitem__( (typeInfo)arg1, (int)arg2) -> typeInfo :
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> __getitem__(class kdlib::TypeInfo {lvalue},unsigned __int64)
#
# __getitem__( (typeInfo)arg1, (str)arg2) -> typeInfo :
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> __getitem__(class kdlib::TypeInfo {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法typeInfo .__ init__
#
# __init__( (object)arg1, (str)arg2) -> object :
#
#     C++ signature :
#         void * __ptr64 __init__(class boost::python::api::object,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法类型Info .__ len__
#
# __len__( (typeInfo)arg1) -> int :
#
#     C++ signature :
#         unsigned __int64 __len__(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo .__ str__
#
# __str__( (typeInfo)arg1) -> str :
#     Return type as a printable string
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > __str__(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.append
#
# append( (typeInfo)arg1, (str)arg2, (typeInfo)arg3) -> None :
#     Add a new field to custom defined struct
#
#     C++ signature :
#         void append(class kdlib::TypeInfo {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >,class boost::shared_ptr<class kdlib::TypeInfo> {lvalue})
#
#
# 方法typeInfo.arrayOf
#
# arrayOf( (typeInfo)arg1, (int)arg2) -> typeInfo :
#     Return array of the type
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> arrayOf(class kdlib::TypeInfo {lvalue},unsigned __int64)
#
#
# 方法typeInfo.baseClass
#
# baseClass( (typeInfo)arg1, (str)arg2) -> typeInfo :
#     Return a base class's type by name
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> baseClass(class kdlib::TypeInfo {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
# baseClass( (typeInfo)arg1, (int)arg2) -> typeInfo :
#     Return a base class's type by index
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> baseClass(class kdlib::TypeInfo {lvalue},unsigned __int64)
#
#
# 方法typeInfo.baseClassOffset
#
# baseClassOffset( (typeInfo)arg1, (str)arg2) -> int :
#     Return a base class offset by name
#
#     C++ signature :
#         unsigned long baseClassOffset(class kdlib::TypeInfo {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
# baseClassOffset( (typeInfo)arg1, (int)arg2) -> int :
#     Return a base class offset by index
#
#     C++ signature :
#         unsigned long baseClassOffset(class kdlib::TypeInfo {lvalue},unsigned __int64)
#
#
# 方法typeInfo.baseClasses
#
# baseClasses( (typeInfo)arg1) -> list :
#     Return list of tuples ( baseClassName, baseClassOffset, baseClassType)
#
#     C++ signature :
#         class boost::python::list baseClasses(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.bitOffset
#
# bitOffset( (typeInfo)arg1) -> int :
#     Return bit field's offset
#
#     C++ signature :
#         unsigned long bitOffset(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.bitWidth
#
# bitWidth( (typeInfo)arg1) -> int :
#     Return bit field's length
#
#     C++ signature :
#         unsigned long bitWidth(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.deref
#
# deref( (typeInfo)arg1) -> typeInfo :
#     Return type of pointer
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> deref(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.field
#
# field( (typeInfo)arg1, (int)arg2) -> typeInfo :
#     Return field's type by index
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> field(class kdlib::TypeInfo {lvalue},unsigned __int64)
#
# field( (typeInfo)arg1, (str)arg2) -> typeInfo :
#     Return field's type
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> field(class kdlib::TypeInfo {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法typeInfo.fieldName
#
# fieldName( (typeInfo)arg1, (int)arg2) -> str :
#     Return name of struct field by index
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > fieldName(class kdlib::TypeInfo {lvalue},unsigned __int64)
#
#
# 方法typeInfo.fieldOffset
#
# fieldOffset( (typeInfo)arg1, (str)arg2) -> int :
#     Return offset of the nonstatic field
#
#     C++ signature :
#         unsigned long fieldOffset(class kdlib::TypeInfo {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
# fieldOffset( (typeInfo)arg1, (int)arg2) -> int :
#     Return offset of the nonstatic field by index
#
#     C++ signature :
#         unsigned long fieldOffset(class kdlib::TypeInfo {lvalue},unsigned __int64)
#
#
# 方法typeInfo.fields
#
# fields( (typeInfo)arg1) -> list :
#     Return list of tuple ( filedName, fieldType )
#
#     C++ signature :
#         class boost::python::list fields(class boost::shared_ptr<class kdlib::TypeInfo>)
#
#
# 方法typeInfo.getCallingConvention
#
# getCallingConvention( (typeInfo)arg1) -> callingConvention :
#     Returns an indicator of a methods calling convention: callingConvention
#
#     C++ signature :
#         enum kdlib::CallingConventionType getCallingConvention(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.getClassParent
#
# getClassParent( (typeInfo)arg1) -> typeInfo :
#     Return class parent
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> getClassParent(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.getNumberBaseClasses
#
# getNumberBaseClasses( (typeInfo)arg1) -> int :
#     Return number of base classes
#
#     C++ signature :
#         unsigned __int64 getNumberBaseClasses(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.getNumberFields
#
# getNumberFields( (typeInfo)arg1) -> int :
#     Return number of fields
#
#     C++ signature :
#         unsigned __int64 getNumberFields(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.getNumberMethods
#
# getNumberMethods( (typeInfo)arg1) -> int :
#     Return number of methods
#
#     C++ signature :
#         unsigned __int64 getNumberMethods(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.getTemplateArgs
#
# getTemplateArgs( (typeInfo)arg1) -> list :
#     Return list if template arguments
#
#     C++ signature :
#         class boost::python::list getTemplateArgs(class boost::shared_ptr<class kdlib::TypeInfo>)
#
#
# 方法typeInfo.getTypedVar
#
# getTypedVar( (typeInfo)arg1, (object)arg2) -> typedVar :
#     return typedVar instance
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> getTypedVar(class boost::shared_ptr<class kdlib::TypeInfo>,class boost::python::api::object {lvalue})
#
#
# 方法typeInfo.hasField
#
# hasField( (typeInfo)arg1, (str)arg2) -> bool :
#     Return True if type has a field with the specified name
#
#     C++ signature :
#         bool hasField(class boost::shared_ptr<class kdlib::TypeInfo> {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法typeInfo.hasMethod
#
# hasMethod( (typeInfo)arg1, (str)arg2) -> bool :
#     Return True if type has a method with the specified name
#
#     C++ signature :
#         bool hasMethod(class boost::shared_ptr<class kdlib::TypeInfo> {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法typeInfo.isArray
#
# isArray( (typeInfo)arg1) -> bool :
#     Return flag: type is array
#
#     C++ signature :
#         bool isArray(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.isBase
#
# isBase( (typeInfo)arg1) -> bool :
#     Return flag: type is base
#
#     C++ signature :
#         bool isBase(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.isBitField
#
# isBitField( (typeInfo)arg1) -> bool :
#     Return flag: type is bit field
#
#     C++ signature :
#         bool isBitField(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.isConstField
#
# isConstField( (typeInfo)arg1, (str)arg2) -> bool :
#     Return True if a field is a const field by field name
#
#     C++ signature :
#         bool isConstField(class boost::shared_ptr<class kdlib::TypeInfo>,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
# isConstField( (typeInfo)arg1, (int)arg2) -> bool :
#     Return True if a field is a const field by field name
#
#     C++ signature :
#         bool isConstField(class boost::shared_ptr<class kdlib::TypeInfo>,unsigned __int64)
#
#
# 方法typeInfo.isConstant
#
# isConstant( (typeInfo)arg1) -> bool :
#     Return flag: type is constant
#
#     C++ signature :
#         bool isConstant(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.isEnum
#
# isEnum( (typeInfo)arg1) -> bool :
#     Return flag: type is enum
#
#     C++ signature :
#         bool isEnum(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.isFunction
#
# isFunction( (typeInfo)arg1) -> bool :
#     Return flag: type is function
#
#     C++ signature :
#         bool isFunction(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.isNoType
#
# isNoType( (typeInfo)arg1) -> bool :
#     Return true if type is virtual table
#
#     C++ signature :
#         bool isNoType(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.isPointer
#
# isPointer( (typeInfo)arg1) -> bool :
#     Return flag: type is pointer
#
#     C++ signature :
#         bool isPointer(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.isStaticField
#
# isStaticField( (typeInfo)arg1, (str)arg2) -> bool :
#     Return True if a field is a static field by field name
#
#     C++ signature :
#         bool isStaticField(class boost::shared_ptr<class kdlib::TypeInfo>,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
# isStaticField( (typeInfo)arg1, (int)arg2) -> bool :
#     Return True if a field is a static field by field name
#
#     C++ signature :
#         bool isStaticField(class boost::shared_ptr<class kdlib::TypeInfo>,unsigned __int64)
#
#
# 方法typeInfo.isTemplate
#
# isTemplate( (typeInfo)arg1) -> bool :
#     Return true if type is template
#
#     C++ signature :
#         bool isTemplate(class boost::shared_ptr<class kdlib::TypeInfo>)
#
#
# 方法typeInfo.isUserDefined
#
# isUserDefined( (typeInfo)arg1) -> bool :
#     Return flag: type is UDT
#
#     C++ signature :
#         bool isUserDefined(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.isVoid
#
# isVoid( (typeInfo)arg1) -> bool :
#     Return flag: type is void
#
#     C++ signature :
#         bool isVoid(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.isVtbl
#
# isVtbl( (typeInfo)arg1) -> bool :
#     Return true if no type is specified
#
#     C++ signature :
#         bool isVtbl(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.members
#
# members( (typeInfo)arg1) -> list :
#     Return list of tuple ( memberName, fieldType ). Only defined member, not inherited from base class
#
#     C++ signature :
#         class boost::python::list members(class boost::shared_ptr<class kdlib::TypeInfo>)
#
#
# 方法typeInfo.method
#
# method( (typeInfo)arg1, (str)arg2) -> typeInfo :
#     Return method's type by name
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> method(class kdlib::TypeInfo {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
# method( (typeInfo)arg1, (int)arg2) -> typeInfo :
#     Return method's by index
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> method(class kdlib::TypeInfo {lvalue},unsigned __int64)
#
#
# 方法typeInfo.methodName
#
# methodName( (typeInfo)arg1, (int)arg2) -> str :
#     Return method's name
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > methodName(class kdlib::TypeInfo {lvalue},unsigned __int64)
#
#
# 方法typeInfo.name
#
# name( (typeInfo)arg1) -> str :
#     Return type name
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > name(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.ptrTo
#
# ptrTo( (typeInfo)arg1 [, (int)ptrSize]) -> typeInfo :
#     Return pointer to the type
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> ptrTo(class kdlib::TypeInfo {lvalue} [,unsigned __int64])
#
#
# 方法typeInfo.scopeName
#
# scopeName( (typeInfo)arg1) -> str :
#     Return name of type scope ( module name )
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > scopeName(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.size
#
# size( (typeInfo)arg1) -> int :
#     Return type size
#
#     C++ signature :
#         unsigned __int64 size(class kdlib::TypeInfo {lvalue})
#
#
# 方法typeInfo.staticOffset
#
# staticOffset( (typeInfo)arg1, (str)arg2) -> int :
#     Return offset of the static field
#
#     C++ signature :
#         unsigned __int64 staticOffset(class kdlib::TypeInfo {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 类typeInfoProvider
# Get abstaract access to different type info sources
#
# 基类：
# 实例
#
# 方法：
#
# __getattr__
# __iter__
# getTypeByName
# typeIterator
#
#
#
# 方法typeInfoProvider .__ getattr__
#
# __getattr__( (typeInfoProvider)arg1, (str)arg2) -> typeInfo :
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> __getattr__(class kdlib::TypeInfoProvider {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法typeInfoProvider .__ iter__
#
# __iter__( (typeInfoProvider)arg1) -> typeInfoProviderIterator :
#
#     C++ signature :
#         class pykd::TypeInfoProviderIterator * __ptr64 __iter__(class kdlib::TypeInfoProvider {lvalue})
#
#
# 方法typeInfoProvider.getTypeByName
#
# getTypeByName( (typeInfoProvider)arg1, (str)arg2) -> typeInfo :
#     Get type info by it's name
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> getTypeByName(class kdlib::TypeInfoProvider {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法typeInfoProvider.typeIterator
#
# typeIterator( (typeInfoProvider)arg1, (str)arg2) -> typeInfoProviderIterator :
#     Return type iterator with specified mask
#
#     C++ signature :
#         class pykd::TypeInfoProviderIterator * __ptr64 typeIterator(class kdlib::TypeInfoProvider {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 类typeInfoProviderIterator
# iterator for type provider
#
# 基类：
# 实例
#
# 方法：
#
# __iter__
# __下一个__
#
#
#
# 方法typeInfoProviderIterator .__ iter__
#
# __iter__( (object)arg1) -> object :
#
#     C++ signature :
#         class boost::python::api::object __iter__(class boost::python::api::object)
#
#
# 方法typeInfoProviderIterator .__ next__
#
# __next__( (typeInfoProviderIterator)arg1) -> typeInfo :
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypeInfo> __next__(class pykd::TypeInfoProviderIterator {lvalue})
#
#
# 类类型Var
# Class of non-primitive type object, child class of typeClass. Data from target is copied into object instance
#
# 基类：
# numVariant
#
# 方法：
#
# __布尔__
# __呼叫__
# __包含__
# __dir__
# __getattr__
# __getitem__
# __在里面__
# __iter__
# __len__
# __setattr__
# __setitem__
# __str__
# 呼叫
# castTo
# 取消引用
# 领域
# fieldName
# fieldOffset
# 领域
# getAddress
# getDebugEnd
# getDebugStart
# getLocation
# getNumberFields
# hasField
# hasMethod
# 成员
# 方法
# rawBytes
# setField
# 大小
# 类型
#
#
#
# 方法类型为Var .__ bool__
#
# __bool__( (typedVar)arg1) -> bool :
#
#     C++ signature :
#         bool __bool__(class kdlib::TypedVar {lvalue})
#
#
# 方法类型为Var .__ call__
#
# object __call__(tuple args, dict kwds) :
#
#     C++ signature :
#         object __call__(tuple args, dict kwds)
#
#
# 类型为Var .__ contains__的方法
#
# __contains__( (typedVar)arg1, (str)arg2) -> bool :
#
#     C++ signature :
#         bool __contains__(class boost::shared_ptr<class kdlib::TypedVar> {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法类型为Var .__ dir__
#
# __dir__( (typedVar)arg1) -> list :
#
#     C++ signature :
#         class boost::python::list __dir__(class kdlib::TypedVar {lvalue})
#
#
# 方法类型为Var .__ getattr__
#
# __getattr__( (typedVar)arg1, (str)arg2) -> typedVar :
#     Return field of structure as an object attribute
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> __getattr__(class kdlib::TypedVar {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法类型为Var .__ getitem__
#
# __getitem__( (typedVar)arg1, (int)arg2) -> typedVar :
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> __getitem__(class kdlib::TypedVar {lvalue},long)
#
# __getitem__( (typedVar)arg1, (str)arg2) -> typedVar :
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> __getitem__(class kdlib::TypedVar {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法类型为Var .__ init__
#
# __init__( (object)arg1, (str)arg2) -> object :
#
#     C++ signature :
#         void * __ptr64 __init__(class boost::python::api::object,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
# __init__( (object)arg1, (str)arg2, (object)arg3) -> object :
#
#     C++ signature :
#         void * __ptr64 __init__(class boost::python::api::object,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >,class boost::python::api::object {lvalue})
#
# __init__( (object)arg1, (typeInfo)arg2, (object)arg3) -> object :
#
#     C++ signature :
#         void * __ptr64 __init__(class boost::python::api::object,class boost::shared_ptr<class kdlib::TypeInfo>,class boost::python::api::object {lvalue})
#
# __init__( (object)arg1, (str)arg2, (str)arg3) -> object :
#
#     C++ signature :
#         void * __ptr64 __init__(class boost::python::api::object,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >,class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法类型为Var .__ iter__
#
# __iter__( (typedVar)arg1) -> typedVarIterator :
#
#     C++ signature :
#         class pykd::TypedVarIterator * __ptr64 __iter__(class boost::shared_ptr<class kdlib::TypedVar> {lvalue})
#
#
# 方法类型为Var .__ len__
#
# __len__( (typedVar)arg1) -> int :
#
#     C++ signature :
#         unsigned __int64 __len__(class kdlib::TypedVar {lvalue})
#
#
# 方法类型为Var .__ setattr__
#
# __setattr__( (typedVar)arg1, (str)arg2, (object)arg3) -> None :
#
#     C++ signature :
#         void __setattr__(class kdlib::TypedVar {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >,class boost::python::api::object {lvalue})
#
#
# 方法类型为Var .__ setitem__
#
# __setitem__( (typedVar)arg1, (int)arg2, (object)arg3) -> None :
#
#     C++ signature :
#         void __setitem__(class kdlib::TypedVar {lvalue},long,class boost::python::api::object {lvalue})
#
# __setitem__( (typedVar)arg1, (str)arg2, (object)arg3) -> None :
#
#     C++ signature :
#         void __setitem__(class kdlib::TypedVar {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >,class boost::python::api::object {lvalue})
#
#
# 方法类型为Var .__ str__
#
# __str__( (typedVar)arg1) -> str :
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > __str__(class kdlib::TypedVar {lvalue})
#
#
# 方法类型为Var.call
#
# object call(tuple args, dict kwds) :
#
#     C++ signature :
#         object call(tuple args, dict kwds)
#
#
# 方法类型为Var.castTo
#
# castTo( (typedVar)arg1, (str)arg2) -> typedVar :
#     Cast variable to the type and return new typedVar instance
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> castTo(class kdlib::TypedVar {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
# castTo( (typedVar)arg1, (typeInfo)arg2) -> typedVar :
#     Cast variable to the type and return new typedVar instance
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> castTo(class kdlib::TypedVar {lvalue},class boost::shared_ptr<class kdlib::TypeInfo>)
#
#
# 方法类型为Var.deref
#
# deref( (typedVar)arg1) -> typedVar :
#     Return value by pointer
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> deref(class kdlib::TypedVar {lvalue})
#
#
# 方法类型为Var.field
#
# field( (typedVar)arg1, (str)arg2) -> typedVar :
#     Return field of structure
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> field(class kdlib::TypedVar {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
# field( (typedVar)arg1, (int)arg2) -> typedVar :
#     Return field of structure or array
#
#     C++ signature :
#         class boost::shared_ptr<class kdlib::TypedVar> field(class kdlib::TypedVar {lvalue},long)
#
#
# 方法类型为Var.fieldName
#
# fieldName( (typedVar)arg1, (int)arg2) -> str :
#     Return name of struct field by index
#
#     C++ signature :
#         class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > fieldName(class kdlib::TypedVar {lvalue},long)
#
#
# 方法类型为Var.fieldOffset
#
# fieldOffset( (typedVar)arg1, (str)arg2) -> int :
#     Return target field offset
#
#     C++ signature :
#         unsigned long fieldOffset(class kdlib::TypedVar {lvalue},class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> >)
#
#
# 方法类型为Var.fields
#
# fields( (typedVar)arg1) -> list :
#     Return list of tuple ( filedName, fieldOffset, fieldValue )
#
#     C++ signature :
#         class boost::python::list fields(class boost::shared_ptr<class kdlib::TypedVar>)
#
#
# 方法typedVar.getAddress
#
# getAddress( (typedVar)arg1) -> int :
#     Return virtual address
#
#     C++ signature :
#         unsigned __int64 getAddress(class kdlib::TypedVar {lvalue})
#
#
# 方法typedVar.getDebugEnd
#
# getDebugEnd( (typedVar)arg1) -> int :
#     Return beginning location of the function's epilogue code (virtual address)
#
#     C++ signature :
#         unsigned __int64 getDebugEnd(class kdlib::TypedVar {lvalue})
#
#
# 方法类型为Var.getDebugStart
#
# getDebugStart( (typedVar)arg1) -> int :
#     Return end location of the function's prologue code (virtual address)
#
#     C++ signature :
#         unsigned __int64 getDebugStart(class kdlib::TypedVar {lvalue})
#
#
# 方法typedVar.getLocation
#
# getLocation( (typedVar)arg1) -> tuple :
#     Return location of the varibale
#
#     C++ signature :
#         class boost::python::tuple getLocation(class kdlib::TypedVar {lvalue})
#
#
# 方法typedVar.getNumberFields
#
# getNumberFields( (typedVar)arg1) -> int :
#     Return number of fields
#
#     C++ signature :
#         unsigned __int64 getNumberFields(class kdlib::TypedVar {lvalue})