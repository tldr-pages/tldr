# protoc

> Parse Google Protobuf `.proto` files and generate output in the specified language.
> More information: <https://developers.google.com/protocol-buffers>.

- Generate Python code from a `.proto` file:

`protoc --python_out={{path/to/output_directory}} {{input_file.proto}}`

- Generate Java code from a `.proto` file that imports other `.proto` files:

`protoc --java_out={{path/to/output_directory}} --proto_path={{path/to/import_search_path}} {{input_file.proto}}`

- Generate code for multiple languages:

`protoc --csharp_out={{path/to/c#_output_directory}} --js_out={{path/to/js_output_directory}} {{input_file.proto}}`

- Encode a text-format message into a protocol message from a `.proto` file:

`protoc --encode={{TypeName}} {{input_file.proto}} < {{message.txt}}`

- Decode a protocol message into text-format from a `.proto` file:

`protoc --decode={{TypeName}} {{input_file.proto}} < {{message.bin}}`

- Decode a protocol message into raw tag/value pairs:

`protoc --decode_raw < {{message.bin}}`
