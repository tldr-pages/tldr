# flatc

> Compile FlatBuffers schemas to language-specific code and convert between binary and JSON.
> More information: <https://flatbuffers.dev/flatc/>.

- Generate C++ code from a FlatBuffers schema:

`flatc --cpp {{path/to/schema.fbs}}`

- Generate code for a schema in a specific language and write it to a directory:

`flatc --{{java|python|go|rust|swift}} -o {{path/to/output_directory}} {{path/to/schema.fbs}}`

- Generate code for a schema that imports other schemas:

`flatc --cpp -I {{path/to/import_directory}} {{path/to/schema.fbs}}`

- Generate code for multiple languages:

`flatc --cpp --python --ts -o {{path/to/output_directory}} {{path/to/schema.fbs}}`

- Serialize JSON data to a FlatBuffer binary using a schema:

`flatc --binary {{path/to/schema.fbs}} {{path/to/data.json}}`

- Convert a FlatBuffer binary to JSON using a schema:

`flatc --json {{path/to/schema.fbs}} -- {{path/to/data.bin}}`
