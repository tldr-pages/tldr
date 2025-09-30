# zlib-flate

> 原始 zlib 压缩和解压缩程序。
> `qpdf` 的一部分。
> 更多信息：<https://manned.org/zlib-flate>.

- 压缩一个文件：

`zlib-flate -compress < {{路径/到/输入_文件}} > {{路径/到/压缩.zlib}}`

- 解压缩一个文件：

`zlib-flate -uncompress < {{路径/到/压缩.zlib}} > {{路径/到/输出_文件}}`

- 使用指定的压缩级别压缩文件。0=最快（最差），9=最慢（最佳）：

`zlib-flate -compress={{压缩级别}} < {{路径/到/输入_文件}} > {{路径/到/压缩.zlib}}`
