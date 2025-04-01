# rhash

> 计算或校验常见的消息摘要。
> 更多信息：<https://rhash.sourceforge.net/manpage.php>.

- 计算文件的默认 CRC32 摘要：

`rhash {{path/to/file}}`

- 递归处理目录以生成使用 SHA1 的 SFV 文件：

`rhash --sha1 --recursive {{path/to/folder}} > {{path/to/output.sfv}}`

- 根据 SFV 文件验证文件的完整性：

`rhash --check {{path/to/file.sfv}}`

- 计算文本消息的 SHA3 摘要：

`rhash --sha3-256 --message '{{message}}'`

- 计算文件的 CRC32 摘要并使用 BSD 格式以 base64 编码输出：

`rhash --base64 --bsd {{path/to/file}}`

- 使用自定义输出模板：

`rhash --printf '{{%p\t%s\t%{mtime}\t%m\n}}' {{path/to/file}}`