# dmd

> Official D compiler.
> More information: <https://dlang.org/dmd.html>.

- Build a D source file:

`dmd {{path/to/source.d}}`

- Generate code for all template instantiations:

`dmd -allinst`

- Control bounds checking:

`dmd -boundscheck={{on|safeonly|off}}`

- List information on all available checks:

`dmd -check={{h|help|?}}`

- Turn on colored console output:

`dmd -color`
