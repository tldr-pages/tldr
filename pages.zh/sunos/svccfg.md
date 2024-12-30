# svccfg

> 导入、导出和修改服务配置。
> 更多信息：<https://www.unix.com/man-page/linux/1m/svccfg>。

- 验证配置文件：

`svccfg validate {{path/to/smf_file.xml}}`

- 导出服务配置到文件：

`svccfg export {{servicename}} > {{path/to/smf_file.xml}}`

- 从文件导入/更新服务配置：

`svccfg import {{path/to/smf_file.xml}}`