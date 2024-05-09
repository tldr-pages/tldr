# objcopy

> Copy the contents of an object file to another.
> More information: <https://manned.org/objcopy>.

- Copy data to another file:

`objcopy {{path/to/source_file}} {{path/to/target_file}}`

- Translate object files from one format to another:

`objcopy --input-target={{inputformat}} --output-target={{output_format}} {{path/to/source_file}} {{path/to/target_file}}`

- Strip all symbol information from file:

`objcopy --strip-all {{path/to/source_file}} {{path/to/target_file}}`

- Strip debugging information from file:

`objcopy --strip-debug {{path/to/source_file}} {{path/to/target_file}}`

- Copy a specific section from the source to destination:

`objcopy --only-section={{section}} {{path/to/source_file}} {{path/to/target_file}}`
