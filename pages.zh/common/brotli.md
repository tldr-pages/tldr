# brotli

> 使用 Brotli 压缩/解压缩文件。
> 更多信息：<https://manned.org/brotli>.

- 压缩文件，生成的压缩文件与原文件同目录：

`brotli {{path/to/file}}`

- 解压缩文件，生成的解压文件与原文件同目录：

`brotli {{[-d|--decompress]}} {{path/to/file.br}}`

- 压缩文件并指定输出文件名：

`brotli {{path/to/file}} {{[-o|--output]}} {{path/to/compressed_output_file.br}}`

- 解压缩 Brotli 文件并指定输出文件名：

`brotli {{[-d|--decompress]}} {{path/to/compressed_file.br}} {{[-o|--output]}} {{path/to/output_file}}`

- 指定压缩质量（1=最快（最差），11=最慢（最好））：

`brotli {{[-q|--quality]}} {{11}} {{path/to/file}} {{[-o|--output]}} {{path/to/compressed_output_file.br}}`