# libtool

> A generic library support script that hides the complexity of using shared libraries behind a consistent, portable interface.
> More information: <https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtool>.

- Compile a source file into a `libtool` object:

`libtool {{[c|compile]}} gcc {{[-c|--compile]}} {{path/to/source.c}} {{[-o|--output]}} {{path/to/source.lo}}`

- Create a library or an executable:

`libtool {{[l|link]}} gcc {{[-o|--output]}} {{path/to/library.lo}} {{path/to/source.lo}}`

- Automatically set the library path so that another program can use uninstalled `libtool` generated programs or libraries:

`libtool {{[e|execute]}} gdb {{path/to/program}}`

- Install a shared library:

`libtool {{[i|install]}} cp {{path/to/library.la}} {{path/to/installation_directory}}`

- Complete the installation of `libtool` libraries on the system:

`libtool {{[f|finish]}} {{path/to/installation_directory}}`

- Delete installed libraries or executables:

`libtool {{[u|uninstall]}} {{path/to/installed_library.la}}`

- Delete uninstalled libraries or executables:

`libtool {{[cl|clean]}} rm {{path/to/source.lo}} {{path/to/library.la}}`
