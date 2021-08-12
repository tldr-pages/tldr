# protoc

> Parsează fişierele Google Protobuf `.proto` şi generează ieşire în limba specificată.
> Mai multe informaţii: <https://developers.google.com/protocol-buffers>

- Generarea codului Python dintr-un fișier `.proto`:

`protoc --python_out={{path/to/output_directory}} {{input_file.proto}}`

- Generează cod Java dintr-un fișier `.proto` care importă alte fișiere `.proto`:

`protoc --java_out={{path/to/output_directory}} --proto_path={{path/to/import_search_path}} {{input_file.proto}}`

- Generează cod pentru mai multe limbi:

`protoc --csharp_out={{path/to/c#_output_directory}} --js_out={{path/to/js_output_directory}} {{input_file.proto}}`
