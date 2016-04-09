dbg
===

"Independent" Python Debugger (local/remote client-server & UI agnostic), based on `bdb` and `multiprocessing` (Python Standard Library).

Originally, this module was named `qdb`, due it uses queues (via pipes) internally for RPC, using the `pdb` extension facilities.

The initial main motivation was to decuople the `Pdb` user interface from the low-level Python Debugger framework (`Bdb`), providing a simple communication mechanism in order to implement several frontends (visual IDEs, online web IDEs, etc.).
Already, this project is used in:

 * web2py (integrated to official admin app)
 * rad2py (wxPython IDE in development)

Others attemps include GEdit plugins, and IPython plugins could be comming soon.
Standalone version can be run from the console (like pdb).

To start a debug session for debuggee.py::

    python3 -m dbg debuggee.py

Then start the interactive debugging console::

    python3 -m dbg


To start to debug from inside a running program just do:

```python
import dbg; dbg.debug()
```

Note that `debug` connects to the debugger but doesn't stop immediately (it is designed to be used with visual frontends that set breakpoints at startup). 
Also, you could use the traditional `set_trace` fuction (like in PDB) as a shortcut to start the debugger and stop in the following line:

```python
import dbg; dbg.set_trace()
```

The "server" frontend (debugger) uses `multiprocessing.connection.Listener` and the client "backend" (debuggee) uses `multiprocessing.connection.Client`.
This allows for a single frontend to host multiple debugging sessions (multithreading and multiprocessing could be supported).

Python2 and Python3 compatibility is archived using Pickle 2 standard protocol, so you can debug a py3k app from a py2 IDE.
No dependencies are need.

Per default, it listens on port 6000 (TCP), but that can be configured via environments variables or parameters (host, port, authkey)

