# strip-nondeterminism

> 从文件中移除非确定性信息（例如时间戳）。
> 更多信息：<https://salsa.debian.org/reproducible-builds/strip-nondeterminism>。

- 从文件中移除非确定性信息：

`strip-nondeterminism {{path/to/file}}`

- 从文件中手动指定文件类型并移除非确定性信息：

`strip-nondeterminism --type {{filetype}} {{path/to/file}}`

- 从文件中移除非确定性信息；而不是移除时间戳，将它们设置为指定的 UNIX 时间戳：

`strip-nondeterminism --timestamp {{unix_timestamp}} {{path/to/file}}`
