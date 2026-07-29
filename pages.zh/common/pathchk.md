# pathchk

> 检查路径名的有效性和可移植性。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/pathchk-invocation.html>。

- 检查当前系统中文件路径的有效性：

`pathchk {{路径1 路径2 ...}}`

- 检查更广泛的 POSIX 兼容系统中文件路径的有效性：

`pathchk -p {{路径1 路径2 ...}}`

- 检查所有 POSIX 兼容系统中文件路径的有效性：

`pathchk {{[-p -P|--portability]}} {{路径1 路径2 ...}}`

- 仅检查空路径名或前导破折号（-）：

`pathchk -P {{路径1 路径2 ...}}`
