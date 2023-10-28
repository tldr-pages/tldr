# dmd

> Official D compiler for Linux.
> More information: <https://dlang.org/dmd-linux.html>.

- Build a D source file:

`dmd {{path/to/source.d}}`

- Generate code for all template instantiations:

`dmd -allinst`

- Control if bounds checking is enabled:

`dmd -boundscheck={{on|safeonly|off}}`

- List information on all available checks:

`dmd -check=[h|help|?]`

- Turn colored console output on:

`dmd -color`
