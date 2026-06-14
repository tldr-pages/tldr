# mcs

> Mono C# Կազմող.
> Լրացուցիչ տեղեկություններ. <https://manned.org/mcs>:.

- Կազմեք նշված ֆայլերը.:

`mcs {{path/to/input_file1.cs path/to/input_file2.cs ...}}`

- Նշեք ելքային ծրագրի անվանումը.:

`mcs -out:{{path/to/file.exe}} {{path/to/input_file1.cs path/to/input_file2.cs ...}}`

- Նշեք ելքային ծրագրի տեսակը.:

`mcs -target:{{exe|winexe|library|module}} {{path/to/input_file1.cs path/to/input_file2.cs ...}}`
