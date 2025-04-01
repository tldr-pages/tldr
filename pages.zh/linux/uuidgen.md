# uuidgen

> 生成唯一标识符（UUID）。
> 参见 `uuid`。
> 更多信息：<https://manned.org/uuidgen>。

- 生成一个随机的 UUIDv4：

`uuidgen {{[-r|--random]}}`

- 生成一个基于当前时间的 UUIDv1：

`uuidgen {{[-t|--time]}}`

- 生成一个指定命名空间前缀的名称的 UUIDv5：

`uuidgen {{[-s|--sha1]}} {{[-n|--namespace]}} {{@dns|@url|@oid|@x500}} {{[-N|--name]}} {{object_name}}`