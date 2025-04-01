# expac

> 用于 alpm 数据库的数据提取工具，为基于 pacman 的工具提供类似 printf 的灵活性。
> 参见: `pacman`。
> 更多信息: <https://github.com/falconindy/expac>。

- 列出一个包的依赖项：

`expac -S '%D' {{package}}`

- 列出一个包的可选依赖项：

`expac -S "%o" {{package}}`

- 以 MiB 为单位列出包的下载大小：

`expac -S -H M '%k\t%n' {{package1 package2 ...}}`

- 列出标记为升级的包及其下载大小：

`expac -S -H M '%k\t%n' $(pacman -Qqu) | sort -sh`

- 列出显式安装的包及其可选依赖项：

`expac -d '\n\n' -l '\n\t' -Q '%n\n\t%O' $(pacman -Qeq)`
