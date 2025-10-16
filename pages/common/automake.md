# automake

> Automated Makefile generation for software projects using GNU standards.
> More information: <https://www.gnu.org/software/automake/manual/automake.html#automake-Invocation>.

- Run automake to regenerate Makefiles after editing `Makefile.am`:

`automake`

- Generate `Makefile.in` for a non-GNU project (foreign mode):

`automake --foreign`

- Add verbose output for debugging:

`automake {{[-v|--verbose]}}`

- Display help:

`automake --help`

- Add missing standard files (INSTALL, COPYING, depcomp, etc.):

`automake {{[-a|--add-missing]}}`
