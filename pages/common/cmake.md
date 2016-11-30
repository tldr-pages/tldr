# cmake

> CMake is a cross-platform build system generator.

Make a project in the same directory as the source:

```
cmake
make
```

Make a project in a subdirectory, required for some projects:

```
mkdir build
cd build
cmake ../
make
```

To run cmake in interactive mode (It will ask you for each variable, 
instead of relying on defaults):

`cmake -i`


