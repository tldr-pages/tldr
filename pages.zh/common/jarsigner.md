# jarsigner

> 签署和验证 Java 档案 (JAR) 文件。
> 更多信息：<https://docs.oracle.com/en/java/javase/20/docs/specs/man/jarsigner.html>。

- 签署一个 JAR 文件：

`jarsigner {{path/to/file.jar}} {{keystore_alias}}`

- 使用特定算法签署 JAR 文件：

`jarsigner -sigalg {{algorithm}} {{path/to/file.jar}} {{keystore_alias}}`

- 验证 JAR 文件的签名：

`jarsigner -verify {{path/to/file.jar}}`