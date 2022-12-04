# gnatprep

> Preprocessor for Ada source code files (part of the GNAT toolchain).
> More information: <https://gcc.gnu.org/onlinedocs/gnat_ugn/Preprocessing-with-gnatprep.html>.

- Use symbol definitions from a file:

`gnatprep {{path/to/file1 path/to/file2 ...}}`

- Specify symbol values in the command line:

`gnatprep -D{{name}}={{value}} {{path/to/file1 path/to/file2 ...}}`
