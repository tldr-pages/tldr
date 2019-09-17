# LD_PRELOAD

> Linking shared object which will be loaded before any other library (including the C runtime libc.so).

- Capture system call on ls command:

`LD_PRELOAD=</path/to/shared_object.so> /bin/ls`