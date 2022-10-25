# protoc

> 解析 Google Protobuf `.proto` 文件并生成指定语言的输出。
> 更多信息：<https://developers.google.com/protocol-buffers>.

- 从 `.proto` 文件生成 Python 代码：

`protoc --python_out={{路径/到/输出目录}} {{输入文件.proto}}`

- 从一个导入其他 `.proto` 文件的 `.proto` 文件生成 Java 代码:

`protoc --java_out={{路径/到/输出目录}} --proto_path={{路径/到/导入搜索路径}} {{输入文件.proto}}`

- 生成多种语言的代码：

`protoc --csharp_out={{路径/到/c#_输出目录}} --js_out={{路径/到/js_输出目录}} {{输入文件.proto}}`
