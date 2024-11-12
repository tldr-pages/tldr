# objcopy

> Copy the contents of an object file to another file.
> More information: <https://manned.org/objcopy>.

- Copy data to another file:

`objcopy {{path/to/source_file}} {{path/to/target_file}}`

- Translate object files from one format to another:

`objcopy --input-target={{input_format}} --output-target {{output_format}} {{path/to/source_file}} {{path/to/target_file}}`

- Strip all symbol information from the file:

`objcopy --strip-all {{path/to/source_file}} {{path/to/target_file}}`

- Strip debugging information from the file:

`objcopy --strip-debug {{path/to/source_file}} {{path/to/target_file}}`

- Copy a specific section from the source file to the destination file:

`objcopy --only-section {{section}} {{path/to/source_file}} {{path/to/target_file}}`
