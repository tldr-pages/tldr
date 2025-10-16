# llvm

> Collection of modular and reusable compiler and toolchain technologies.
> More information: <https://llvm.org>.

- Display version information:

`llvm-config --version`

- Display the installation prefix for LLVM:

`llvm-config --prefix`

- Display the C++ compiler flags:

`llvm-config --cxxflags`

- Display the linker flags:

`llvm-config --ldflags`

- Display libraries needed to link against LLVM components:

`llvm-config --libs {{component1 component2 ...}}`

- List available LLVM components:

`llvm-config --components`

- Display the system libraries needed to link:

`llvm-config --system-libs`

- Display the compilation and linking flags for a program:

`llvm-config --cxxflags --ldflags --libs {{core}}`
