# gnucash-cli

> GnuCash 的命令行版本。
> 更多信息：<https://gnucash.org>.

- 获取文件中指定的货币和股票的报价并打印：

`gnucash-cli --quotes get {{path/to/file.gnucash}}`

- 生成特定类型的财务报告，由 `--name` 指定：

`gnucash-cli --report run --name "{{资产负债表}}" {{path/to/file.gnucash}}`