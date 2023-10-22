# pabcnetcclear

> Preprocess and compile PascalABC.NET source files.
> More information: <http://pascalabc.net>.

- Compile the specified source file into an executable with the same name:

`pabcnetcclear {{path\to\source_file.pas}}`

- Compile the specified source file into an executable with the specified name:

`pabcnetcclear /Output:{{path\to\_file.exe}} {{path\to\source_file.pas}}`

- Compile the specified source file into an executable with the same name along with/without debug information:

`pabcnetcclear /Debug:{{0|1}} {{path\to\source_file.pas}}`

- Allow units to be searched in the specified path while compiling the source file into an executable with the same name:

`pabcnetcclear /SearchDir:{{path\to\directory}} {{path\to\source_file.pas}}`

- Compile the specified source file into an executable, defining a symbol:

`pabcnetcclear /Define:{{symbol}} {{path\to\source_file.pas}}`
