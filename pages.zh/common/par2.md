# par2

> 使用 PAR 2.0 兼容的校验文件（.par2 文件）进行文件验证和修复。
> 更多信息：<https://github.com/Parchive/par2cmdline/>.

- 使用指定的冗余百分比创建校验文件：

`par2 create -r{{1..100}} -- {{path/to/file}}`

- 使用指定数量的卷文件（除索引文件外）创建校验文件：

`par2 create -n{{1..32768}} -- {{path/to/file}}`

- 使用校验文件验证文件：

`par2 verify -- {{path/to/file.par2}}`

- 使用校验文件修复文件：

`par2 repair -- {{path/to/file.par2}}`
