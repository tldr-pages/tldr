# protoc

> 解析 Google Protobuf `.proto` 文件并生成指定语言的输出。
> 更多信息：<https://developers.google.com/protocol-buffers>。

- 从 `.proto` 文件生成 Python 代码：

`protoc --python_out={{path/to/output_directory}} {{input_file.proto}}`

- 从导入其他 `.proto` 文件的 `.proto` 文件生成 Java 代码：

`protoc --java_out={{path/to/output_directory}} --proto_path={{path/to/import_search_path}} {{input_file.proto}}`

- 为多种语言生成代码：

`protoc --csharp_out={{path/to/c#_output_directory}} --js_out={{path/to/js_output_directory}} {{input_file.proto}}`