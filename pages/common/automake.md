# automake

> Automated Makefile generation for software projects using GNU standards.
> More information: <https://www.gnu.org/software/automake/manual/automake.html#automake-Invocation>.

- Create a template Makefile.in from Makefile.am:

`automake {{path/to/Makefile.am}}`

- Run automake to regenerate Makefiles after editing Makefile.am:

`automake`

- Generate Makefile.in for a non-GNU project (foreign mode):

`automake --foreign {{path/to/Makefile.am}}`

- Add verbose output for debugging:

`automake {{[-v|--verbose]}}`

- Display help:

`automake --help`

- Specify an alternate directory for output files:

`automake --output-dir {{path/to/output_directory}}`

- Generate Makefile.in for multiple directories (with subdir support):

`automake {{[-a|--add-missing]}}`
