gdb
===

Independent remote client-server Python Debugger, based on `bdb` and `multiprocessing` (Python's StandardLibrary).
Originally, this module was named `qdb`, due it uses queues (via pipes) internally.

Used in:

 * web2py (integrated to official admin app)
 * rad2py (wxPython IDE in development)

Standalone version can be run from the console (like pdb).

To start a debug session for debuggee.py::

    python3 -m dbg debuggee.py

Then start the console client::

    python3 -m dbg


To start to debug from inside a running program just do:

```python
import dbg; dbg.debug()
```

Note that `debug` connects to the debugger but doesn't stop immediately (it is designed to be used with visual frontends that set breakpoints at startup). 
Also, you could use `set_trace` as a shortcut to start the debugger and stop in the following line:

```python
import dbg; dbg.set_trace()
```

The "server" frontend (debugger) uses `multiprocessing.connection.Listener` and the client "backend" (debuggee) uses `multiprocessing.connection.Client`.
This allows for a single frontend to host multiple debugging sessions (multithreading and multiprocessing could be supported).

Python2 and Python3 compatibility is archived using Pickle 2 standard protocol, so you can debug a py3k app from a py2 IDE.
No dependencies are need.

Per default, it listen on port 6000 (TCP), but that can be configured via environments variables or parameters (host, port, authkey)

