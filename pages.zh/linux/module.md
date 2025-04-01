# module

> 使用 module 命令修改用户的环境。
> 更多信息：<https://lmod.readthedocs.io/en/latest/010_user.html>.

- 显示可用的模块：

`module avail`

- 按名称搜索模块：

`module avail {{module_name}}`

- 加载模块：

`module load {{module_name}}`

- 显示已加载的模块：

`module list`

- 卸载特定的已加载模块：

`module unload {{module_name}}`

- 卸载所有已加载的模块：

`module purge`

- 指定用户创建的模块：

`module use {{path/to/module_file1 path/to/module_file2 ...}}`
