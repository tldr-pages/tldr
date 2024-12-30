# age-keygen

> 生成 `age` 密钥对。
> 另请参见：用于加密/解密文件的 `age`。
> 更多信息：<https://manned.org/age-keygen>。

- 生成一个密钥对，保存到一个未加密的文件中，并将公钥打印到 `stdout`：

`age-keygen --output {{path/to/file}}`

- 将身份转换为接收者，并将公钥打印到 `stdout`：

`age-keygen -y {{path/to/file}}`