# ar

> 创建、修改和提取 Unix 存档。通常用于静态库（`.a`）和 Debian 包（`.deb`）。
> 另见：`tar`。
> 更多信息：<https://manned.org/ar>。

- E[x]tract 从存档中提取所有成员：

`ar x {{path/to/file.a}}`

- Lis[t] 列出特定存档的内容：

`ar t {{path/to/file.ar}}`

- [r]eplace 或添加特定文件到存档：

`ar r {{path/to/file.deb}} {{path/to/debian-binary path/to/control.tar.gz path/to/data.tar.xz ...}}`

- In[s]ert 对象文件索引（等同于使用 `ranlib`）：

`ar s {{path/to/file.a}}`

- 创建一个包含特定文件和附带对象文件索引的存档：

`ar rs {{path/to/file.a}} {{path/to/file1.o path/to/file2.o ...}}`