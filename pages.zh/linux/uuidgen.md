# uuidgen

> 生成唯一标识符 (UUID)。
> 另请参见 `uuid`。
> 更多信息：<https://manned.org/uuidgen>。

- 创建一个随机 UUIDv4：

`uuidgen --random`

- 创建一个基于当前时间的 UUIDv1：

`uuidgen --time`

- 创建一个带有指定命名空间前缀的 UUIDv5：

`uuidgen --sha1 --namespace {{@dns|@url|@oid|@x500}} --name {{object_name}}`