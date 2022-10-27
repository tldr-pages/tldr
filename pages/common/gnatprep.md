# gnatprep

> Preprocessor for Ada source code files (part of the GNAT toolchain).
> More information: <https://gcc.gnu.org/onlinedocs/gnat_ugn/Preprocessing-with-gnatprep.html>.

- Use symbol definitions from a file:

`gnatprep {{source_file}} {{target_file}} {{definitions_file}}`

- Specify symbol values in the command line:

`gnatprep -D{{name}}={{value}} {{source_file}} {{target_file}}`
