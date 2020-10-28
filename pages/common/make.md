# make

> Task runner for targets described in Makefile.
> Mostly used to control the compilation of an executable from source code.
> More information: <https://www.gnu.org/software/make/manual/make.html>.

- Call the first target specified in the Makefile (usually named "all"):

`make`

- Call a specific target:

`make {{target}}`

- Call a specific target, executing 4 jobs at a time in parallel:

`make -j{{4}} {{target}}`

- Use a specific Makefile:

`make --file {{file}}`

- Execute make from another directory:

`make --directory {{directory}}`

- Force making of a target, even if source files are unchanged:

`make --always-make {{target}}`

- Override variables defined in the Makefile by the environment:

`make --environment-overrides {{target}}`
