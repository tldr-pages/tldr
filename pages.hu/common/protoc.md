# protoc

> A Google Protobuf `.proto` fájlok elemzése és a megadott nyelven történő kimenet generálása. További információ: <https://developers.google.com/protocol-buffers>.

- Python kód generálása a `.proto` fájlból:

`protoc --python_out={{path/to/output_directory}} {{input_file.proto}}`

- Java kód generálása egy `.proto` fájlból, amely más `.proto` fájlokat importál:

`protoc --java_out={{path/to/output_directory}} --proto_path={{path/to/import_search_path}} {{input_file.proto}}`

- Kód generálása több nyelven:

`protoc --csharp_out={{path/to/c#_output_directory}} --js_out={{path/to/js_output_directory}} {{input_file.proto}}`
