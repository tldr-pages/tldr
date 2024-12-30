# Dart

> 管理 Dart 项目。
> 更多信息：<https://dart.dev/tools/dart-tool>。

- 在同名目录中初始化一个新的 Dart 项目：

`dart create {{project_name}}`

- 运行一个 Dart 文件：

`dart run {{path/to/file.dart}}`

- 下载当前项目的依赖：

`dart pub get`

- 运行当前项目的单元测试：

`dart test`

- 更新过时项目的依赖以支持空安全：

`dart pub upgrade --null-safety`

- 将 Dart 文件编译为原生二进制文件：

`dart compile exe {{path/to/file.dart}}`

- 对当前项目应用自动修复：

`dart fix --apply`