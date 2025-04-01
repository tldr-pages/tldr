# setcap

> 设置指定文件的能力。
> 参见: `getcap`。
> 更多信息: <https://manned.org/setcap>。

- 为指定文件设置 `cap_net_raw` 能力（用于使用 RAW 和 PACKET 套接字）:

`setcap '{{cap_net_raw}}' {{path/to/file}}`

- 为文件设置多个能力（能力后的 `ep` 表示“有效和允许”）:

`setcap '{{cap_dac_read_search,cap_sys_tty_config+ep}}' {{path/to/file}}`

- 从文件中移除所有能力:

`setcap -r {{path/to/file}}`

- 验证指定的能力是否当前与指定文件关联:

`setcap -v '{{cap_net_raw}}' {{path/to/file}}`

- 可选的 `-n root_uid` 参数可以用于设置文件能力，仅在具有此根用户 ID 的用户命名空间中使用:

`setcap -n {{root_uid}} '{{cap_net_admin}}' {{path/to/file}}`
