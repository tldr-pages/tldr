# libtoolize

> A tool used in the autotools build system to prepare a package for using `libtool`.
> It performs various tasks, including generating necessary files and directories to integrate `libtool` seamlessly into a project.
> More information: <https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtoolize>.

- Initialize a project for `libtool` by copying necessary files (avoiding symbolic links) and overwriting existing files if needed:

`libtoolize --copy --force`
