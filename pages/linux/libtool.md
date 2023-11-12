# libtool

> Libtool is a generic library support script that hides the complexity of using shared libraries behind a consistent, portable interface.
> More information: <https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtool>.

- Compile a source file into a `libtool` object:

`libtool --mode=compile gcc -c {{path/to/source.c}} -o {{path/to/source.lo}}`

- Create a library or an executable:

`libtool --mode=link gcc -o {{path/to/library.lo}} {{path/to/source.lo}}`

- Automatically set the library path so that another program can use uninstalled `libtool` generated programs or libraries:

`libtool --mode=execute gdb {{path/to/program}}`

- Install a shared library:

`libtool --mode=install cp {{path/to/library.la}} {{path/to/installation_directory}}`

- Complete the installation of `libtool` libraries on the system:

`libtool --mode=finish {{path/to/installation_dir}}`

- Delete installed libraries or executables:

`libtool --mode=uninstall {{path/to/installed_library.la}}`

- Delete uninstalled libraries or executables:

`libtool --mode=clean rm {{path/to/source.lo}} {{path/to/library.la}}`
