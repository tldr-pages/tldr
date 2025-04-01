# tlmgr generate

> 从本地存储的信息重新生成配置文件。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>.

- 重新生成配置文件并存储到指定位置：

`tlmgr generate --dest {{output_file}}`

- 使用本地配置文件重新生成配置文件：

`tlmgr generate --localcfg {{local_configuration_file}}`

- 重新生成配置文件后运行必要的程序：

`tlmgr generate --rebuild-sys`