# brotli

> 使用 Brotli 压缩进行文件的压缩/解压缩。
> 更多信息：<https://github.com/google/brotli>。

- 压缩文件，在文件旁边创建一个压缩版本：

`brotli {{path/to/file}}`

- [d]解压缩文件，在文件旁边创建一个未压缩版本：

`brotli -d {{path/to/file.br}}`

- 压缩文件并指定 [o]utput 文件名：

`brotli {{path/to/file}} -o {{path/to/compressed_output_file.br}}`

- [d]解压缩 Brotli 文件并指定 [o]utput 文件名：

`brotli -d {{path/to/compressed_file.br}} -o {{path/to/output_file}}`

- 指定压缩质量（1=最快（最差），11=最慢（最好））：

`brotli -q {{11}} {{path/to/file}} -o {{path/to/compressed_output_file.br}}`