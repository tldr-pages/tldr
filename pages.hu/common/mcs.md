# mcs

> Mono C# fordító. További információ: <https://manned.org/mcs.1>.

- Fordítsa le a megadott fájlokat:

`mcs {{path/to/input_file1.cs path/to/input_file2.cs ...}}`

- Adja meg a kimeneti program nevét:

`mcs -out:{{path/to/file.exe}} {{path/to/input_file1.cs path/to/input_file2.cs ...}}`

- Adja meg a kimeneti program típusát:

`mcs -target:{{exe|winexe|library|module}} {{path/to/input_file1.cs path/to/input_file2.cs ...}}`
