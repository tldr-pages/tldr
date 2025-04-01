# uuid

> 生成和解析通用唯一标识符（UUID）。
> 另见 `uuidgen`。
> 更多信息：<https://manned.org/uuid>。

- 生成一个基于时间和系统硬件地址（如果存在）的UUIDv1：

`uuid`

- 生成一个基于随机数据的UUIDv4：

`uuid -v {{4}}`

- 一次性生成多个UUIDv4标识符：

`uuid -v {{4}} -n {{number_of_uuids}}`

- 生成一个UUIDv4并指定输出格式：

`uuid -v {{4}} -F {{BIN|STR|SIV}}`

- 生成一个UUIDv4并将输出写入文件：

`uuid -v {{4}} -o {{path/to/file}}`

- 生成一个基于提供的对象名称的UUIDv5，并指定命名空间前缀：

`uuid -v {{5}} ns:{{DNS|URL|OID|X500}} {{object_name}}`

- 解析给定的UUID：

`uuid -d {{uuid}}`
