# par2

> 使用PAR 2.0兼容的奇偶校验档案（.par2文件）进行文件验证和修复。
> 更多信息：<https://github.com/Parchive/par2cmdline/>.

- 创建一个带有设定百分比冗余级别的奇偶校验档案：

`par2 create -r{{1..100}} -- {{path/to/file}}`

- 创建一个具有选定数量卷文件（除了索引文件）的奇偶校验档案：

`par2 create -n{{1..32768}} -- {{path/to/file}}`

- 使用奇偶校验档案验证文件：

`par2 verify -- {{path/to/file.par2}}`

- 使用奇偶校验档案修复文件：

`par2 repair -- {{path/to/file.par2}}`