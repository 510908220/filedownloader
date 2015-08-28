# filedownloader
![文件下载器](http://7xk7ho.com1.z0.glb.clouddn.com/download.jpg)

##下载协议
###http



as_completed里会间接调用到:
```
 lock = thread.allocate_lock()
 lock.acquire()
           
```
lock.acquire()会触发KeyboardInterrupt


urllib.request.urlretrieve(url, output)
requests.get(url,stream=True)

```
ntoskrnl.exe!memset+0x61a
ntoskrnl.exe!KeWaitForMultipleObjects+0xd52
ntoskrnl.exe!KeWaitForMutexObject+0x19f
ntoskrnl.exe!PoStartNextPowerIrp+0xba4
ntoskrnl.exe!PoStartNextPowerIrp+0x1821
ntoskrnl.exe!KeWaitForMultipleObjects+0xf5d
ntoskrnl.exe!KeWaitForMutexObject+0x19f
ntoskrnl.exe!NtWaitForSingleObject+0xde
ntoskrnl.exe!KeSynchronizeExecution+0x3a23
wow64cpu.dll!TurboDispatchJumpAddressEnd+0x6c0
wow64cpu.dll!TurboDispatchJumpAddressEnd+0x4a8
wow64.dll!Wow64SystemServiceEx+0x1ce
wow64.dll!Wow64LdrpInitialize+0x42a
ntdll.dll!RtlFreeHeap+0x1a1a4
ntdll.dll!LdrInitializeThunk+0xe
ntdll.dll!NtWaitForSingleObject+0x15
mswsock.dll+0x76b6
WS2_32.dll!recv+0x79
_socket.pyd+0x2688
_socket.pyd+0x28a6
python34.dll!PyCFunction_Call+0x65
python34.dll!PyEval_GetGlobals+0x6af
python34.dll!PyEval_EvalFrameEx+0x1ff9
python34.dll!PyEval_EvalCodeEx+0x55d
python34.dll!PyFunction_SetAnnotations+0x8e5
python34.dll!PyObject_Call+0x5b
python34.dll!PyMethod_New+0x5f2
python34.dll!PyObject_Call+0x5b
python34.dll!PyObject_CallMethodObjArgs+0x54
python34.dll!PyErr_SetInterrupt+0xc4b7
python34.dll!PyErr_SetInterrupt+0xc5ac
python34.dll!PyCFunction_Call+0x52
python34.dll!PyEval_GetGlobals+0x6af
python34.dll!PyEval_EvalFrameEx+0x1ff9
python34.dll!PyEval_EvalCodeEx+0x55d
python34.dll!PyFunction_SetAnnotations+0x8e5
python34.dll!PyObject_Call+0x5b
python34.dll!PyMethod_New+0x5f2
python34.dll!PyObject_Call+0x5b
python34.dll!PyObject_CallMethodObjArgs+0x54
python34.dll!PyErr_SetInterrupt+0xf4e0
python34.dll!PyCFunction_Call+0x52
python34.dll!PyEval_GetGlobals+0x6af
python34.dll!PyEval_EvalFrameEx+0x1ff9
python34.dll!PyEval_EvalCodeEx+0x55d
python34.dll!PyEval_EvalCodeEx+0x693
python34.dll!PyEval_GetGlobals+0x70c
python34.dll!PyEval_EvalFrameEx+0x1ff9
python34.dll!PyEval_EvalCodeEx+0x55d
python34.dll!PyEval_EvalCodeEx+0x693
python34.dll!PyEval_GetGlobals+0x70c
python34.dll!PyEval_EvalFrameEx+0x1ff9
python34.dll!PyStaticMethod_New+0x204
python34.dll!PyEval_EvalFrameEx+0x5a2
python34.dll!PyStaticMethod_New+0x204
python34.dll!PyEval_EvalFrameEx+0x5a2
python34.dll!PyEval_EvalCodeEx+0x55d
python34.dll!PyEval_EvalCodeEx+0x693
python34.dll!PyEval_GetGlobals+0x70c
python34.dll!PyEval_EvalFrameEx+0x1ff9
python34.dll!PyEval_EvalCodeEx+0x62f
python34.dll!PyEval_GetGlobals+0x70c
python34.dll!PyEval_EvalFrameEx+0x1ff9
python34.dll!PyEval_EvalCodeEx+0x62f
python34.dll!PyEval_GetGlobals+0x70c
python34.dll!PyEval_EvalFrameEx+0x1ff9
python34.dll!PyEval_EvalCodeEx+0x55d
python34.dll!PyFunction_SetAnnotations+0x8e5
python34.dll!PyObject_Call+0x5b
python34.dll!PyMethod_New+0x5f2
python34.dll!PyObject_Call+0x5b
python34.dll!PyEval_CallObjectWithKeywords+0x8b
python34.dll!PyErr_SetInterrupt+0xfb9
python34.dll!PySys_FormatStderr+0x420
MSVCR100.dll!_endthreadex+0x3a
MSVCR100.dll!_endthreadex+0xe4
kernel32.dll!BaseThreadInitThunk+0x12
ntdll.dll!RtlInitializeExceptionChain+0x63
ntdll.dll!RtlInitializeExceptionChain+0x36
```