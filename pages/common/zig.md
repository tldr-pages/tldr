# zig

> The Zig compiler and toolchain.
> More information: <https://ziglang.org/documentation/master/>.

- Compile the project in the current directory:

`zig build`

- Compile and run the project in the current directory:

`zig build run`

- Initialize a `zig build` project with library and executable:

`zig init`

- Create and run a test build:

`zig test {{path/to/file.zig}}`

- Cross compile, build and run a project for `x86_64` architecture and `windows` operating system:

`zig build run -fwine -Dtarget=x86_64-windows`

- Reformat Zig source into canonical form:

`zig fmt {{path/to/file.zig}}`

- Translate a C file to `zig`:

`zig translate-c -lc {{path/to/file.c}}`

- Use Zig as a drop-in C++ compiler:

`zig c++ {{path/to/file.cpp}}`
