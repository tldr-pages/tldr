# gprbuild

> A high-level build tool for projects written in Ada and other languages (C/C++/Fortran).
> More information: <https://docs.adacore.com/gprbuild-docs/html/gprbuild_ug.html>.

- Build a project (assuming only one `*.gpr` file exists in the current directory):

`gprbuild`

- Build a specific [P]roject file:

`gprbuild -P{{project_name}}`

- Clean up the build workspace:

`gprclean`

- Install compiled binaries:

`gprinstall --prefix {{path/to/installation/dir}}`
