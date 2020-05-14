# pkg-config

> Return metainformation about installed libraries.

- Get the list of libraries and their dependencies:

`pkg-config --libs {{library1 library2 ...}}`

- Get the list of libraries, their dependencies, and proper cflags for using with gcc:

`pkg-config --cflags --libs {{library1 library2 ...}}`
