# LD_PRELOAD

> Linking shared object which will be loaded before any other library (including the C runtime libc.so).

- Capturing system call on listing command

  `LD_PRELOAD=</path/to/shared_object.so> /bin/ls`

