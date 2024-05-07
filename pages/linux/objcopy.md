# objcopy

> The GNU objcopy utility copies the contents of an object file to another.
> More Information: <https://manned.org/objcopy>.

- Copy data to another file:

`objcopy {{/your/path/to/file/src}} {{/your/path/to/file/destination}}`

- Translate object files from one format to another:

`objcopy --input-target={{inputformat}} --output-target={{output_format}} {{/path/to/your/src}} {{path/to/your/destination}}`

- Strip all symbol information from file:

`objcopy --strip-all {{/path/to/your/src}} {{path/to/your/destination}}`

- Strip debugging information from file:

`objcopy --strip-debug {{/path/to/your/src}} {{path/to/your/destination}}`

- Copy a specific section from the source to destination:

`objcopy --only-section={{section}} {{/path/to/your/src}} {{path/to/your/destination}}`
