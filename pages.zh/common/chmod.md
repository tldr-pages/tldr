# chmod

> 更改文件或目录的访问权限。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html>。

- 给予文件的拥有者[u]执行的权限[e]：

`chmod u+x {{path/to/file}}`

- 给予用户[u]对文件/目录的[r]ead和[w]rite权限：

`chmod u+rw {{path/to/file_or_directory}}`

- 从[group]移除执行权限[e]：

`chmod g-x {{path/to/file}}`

- 给予所有用户[a]读取和执行[r]权限：

`chmod a+rx {{path/to/file}}`

- 给予其他用户[o]（不在文件拥有者组内）与[group]相同的权限：

`chmod o=g {{path/to/file}}`

- 移除所有权限从其他用户[o]：

`chmod o= {{path/to/file}}`

- 递归更改权限，给予[group]和其他用户[o]写入权限：

`chmod -R g+w,o+w {{path/to/directory}}`

- 递归给予所有用户[a]对文件的读取权限和对目录内子目录的执行权限[e]：

`chmod -R a+rX {{path/to/directory}}`