# pabcnetcclear

> Preprocess and compile PascalABC.NET source files.
> More information: <http://pascalabc.net>.

- Compile a given source file into an executable with the same name:

`pabcnetcclear {{path/to/file.pas}}`

- Compile a given source file into an executable with the specified name:

`pabcnetcclear /Output:{{path/to/file.pas}} {{path/to/file.pas}}`

- Compile a given source file into an executable with the same name along with/without debug information:

`pabcnetcclear /Debug:{{0|1}} {{path/to/file.pas}}`

- Allow units to be searched in a path while compiling a given source file into an executable with the same name:

`pabcnetcclear /SearchDir:{{path/to/dir}} {{path/to/file.pas}}`

- Compile a given source file into an executable, defining a symbol:

`pabcnetcclear /Define:{{symbol}} {{path/to/file.pas}}`
