# uuid

> 生成和解码全局唯一标识符（UUID）。
> 另见 `uuidgen`。
> 更多信息：<https://manned.org/uuid>。

- 生成一个 UUIDv1（基于时间和系统的硬件地址，如果存在）：

`uuid`

- 生成一个 UUIDv4（基于随机数据）：

`uuid -v {{4}}`

- 一次生成多个 UUIDv4 标识符：

`uuid -v {{4}} -n {{number_of_uuids}}`

- 生成一个 UUIDv4 并指定输出格式：

`uuid -v {{4}} -F {{BIN|STR|SIV}}`

- 生成一个 UUIDv4 并将输出写入文件：

`uuid -v {{4}} -o {{path/to/file}}`

- 生成一个 UUIDv5（基于提供的对象名称）并指定命名空间前缀：

`uuid -v {{5}} ns:{{DNS|URL|OID|X500}} {{object_name}}`

- 解码给定的 UUID：

`uuid -d {{uuid}}`