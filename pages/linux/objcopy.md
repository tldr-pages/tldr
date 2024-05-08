# objcopy

> Copy the contents of an object file to another.
> More information: <https://manned.org/objcopy>.

- Copy all data from a specific file to another one:

`objcopy {{path/to/file/source_file}} {{path/to/file/target_file}}`

- Translate object files from one format to another:

`objcopy --input-target={{inputformat}} --output-target={{output_format}} {{path/to/your/source_file}} {{path/to/your/target_file}}`

- Strip all symbol information from a specific file:

`objcopy --strip-all {{path/to/your/source_file}} {{path/to/your/target_file}}`

- Strip debugging information from file:

`objcopy --strip-debug {{/path/to/your/source_file}} {{path/to/your/target_file}}`

- Copy a specific section of the source file to the destination file:

`objcopy --only-section={{section}} {{path/to/your/source_file}} {{path/to/your/target_file}}`
