# jarsigner

> 签名并验证 Java 存档（JAR）文件。
> 更多信息：<https://docs.oracle.com/javase/9/tools/jarsigner.htm>.

- 签名一个 `JAR` 文件：

`jarsigner {{path/to/file.jar}} {{keystore_alias}}`

- 使用特定算法对 `JAR` 文件进行签名：

`jarsigner -sigalg {{algorithm}} {{path/to/file.jar}} {{keystore_alias}}`

- 验证 `JAR` 文件的签名：

`jarsigner -verify {{path/to/file.jar}}`
