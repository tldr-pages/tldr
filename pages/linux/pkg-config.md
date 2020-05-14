# pkg-config

> Provide the details of installed libraries for compiling applications.
> More information: <https://www.freedesktop.org/wiki/Software/pkg-config/>.

- Get the list of libraries and their dependencies:

`pkg-config --libs {{library1 library2 ...}}`

- Get the list of libraries, their dependencies, and proper cflags for gcc:

`pkg-config --cflags --libs {{library1 library2 ...}}`
