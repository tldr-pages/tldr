# pathchk

> 检查路径名的有效性和可移植性。
> 更多信息：<https://www.gnu.org/software/coreutils/pathchk>。

- 检查当前系统中路径名的有效性：

`pathchk {{path1 path2 …}}`

- 检查在更广泛的 POSIX 兼容系统上路径名的有效性：

`pathchk -p {{path1 path2 …}}`

- 检查在所有 POSIX 兼容系统上路径名的有效性：

`pathchk --portability {{path1 path2 …}}`

- 仅检查空路径名或以破折号 (-) 开头的路径名：

`pathchk -P {{path1 path2 …}}`