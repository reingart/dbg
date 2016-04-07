gdb / qdb
=========

Queues(Pipe)-based independent remote client-server Python Debugger, based on `bdb` and `multiprocessing` (Python's StandardLibrary).

Used in:

 * web2py (integrated to official admin app)
 * rad2py (wxPython IDE in development)

Standalone version can be run from the console (like pdb).

To start a debug session for debuggee.py::

    python3 -m dbg debuggee.py

Then start the console client::

    python3 -m dbg


To start a debug from inside a running program just do:

```python
import dbg; dbg.debug()
```

The client (debugger) uses `multiprocessing.connection.Listener` and the server (debuggee) uses `multiprocessing.connection.Client`.
Python2 and Python3 compatibility is archived using Pickle 2 standard protocol, so you can debug a py3k app from a py2 IDE.
No dependencies are need.

Per default, it listen on port 6000 (TCP), but that can be configured via environments variables or parameters (host, port, authkey)
