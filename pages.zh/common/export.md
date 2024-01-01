# export

> 命令为当前 shell 中的子进程进行环境变量设置。
> 更多信息：<https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#export>.

- 设置为新的环境变量：

`export {{某变量名}}={{值}}`

- 删除环境变量：

`export -n {{某变量名}}`

- 给 PATH 追加新的路径进去：

`export PATH=$PATH:{{追加的 path 路径}}`
