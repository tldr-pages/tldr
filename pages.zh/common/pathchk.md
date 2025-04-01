# pathchk

> 检查路径名的有效性和可移植性。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/pathchk-invocation.html>。

- 检查路径名在当前系统中的有效性：

`pathchk {{path1 path2 …}}`

- 检查路径名在更大范围的 POSIX 兼容系统中的有效性：

`pathchk -p {{path1 path2 …}}`

- 检查路径名在所有 POSIX 兼容系统中的有效性：

`pathchk --portability {{path1 path2 …}}`

- 仅检查空路径名或引导短划线 (-)：

`pathchk -P {{path1 path2 …}}`
