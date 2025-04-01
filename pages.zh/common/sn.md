# sn

> Mono StrongName 工具，用于签署和验证 IL 程序集。
> 更多信息：<https://manned.org/sn>.

- 生成一个新的 StrongNaming 密钥：

`sn -k {{path/to/key.snk}}`

- 使用指定的私钥重新签署程序集：

`sn -R {{path/to/assembly.dll}} {{path/to/key_pair.snk}}`

- 显示用于签署程序集的私钥的公钥：

`sn -T {{path/to/assembly.exe}}`

- 将公钥提取到文件中：

`sn -e {{path/to/assembly.dll}} {{path/to/output.pub}}`
