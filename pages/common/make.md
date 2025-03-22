# make

> Task runner for targets described in Makefile.
> Mostly used to control the compilation of an executable from source code.
> More information: <https://www.gnu.org/software/make/manual/make.html>.

- Call the first target specified in the Makefile (usually named "all"):

`make`

- Call a specific target:

`make {{target}}`

- Call a specific target, executing 4 jobs at a time in parallel:

`make {{[-j|--jobs]}} {{4}} {{target}}`

- Use a specific Makefile:

`make {{[-f|--file]}} {{path/to/file}}`

- Execute make from another directory:

`make {{[-C|--directory]}} {{path/to/directory}}`

- Force making of a target, even if source files are unchanged:

`make {{[-B|--always-make]}} {{target}}`

- Override a variable defined in the Makefile:

`make {{target}} {{variable}}={{new_value}}`

- Override variables defined in the Makefile by the environment:

`make {{[-e|--environment-overrides]}} {{target}}`
