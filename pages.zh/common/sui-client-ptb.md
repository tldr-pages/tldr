# sui client ptb

> 创建、签名和执行可编程事务块。
> 更多信息：<https://docs.sui.io/references/cli/ptb>.

- 从包和模块中调用 Move 函数：

`sui client ptb --move-call p::m::f "<{{type}}>" args`

- 创建一个包含两个 u64 类型元素的 Move 向量：

`sui client ptb --make-move-vec "<u64>" "[1000,2000]"`

- 拆分一个 gas 代币并将其转移到地址：

`sui client ptb --split-coins gas "[1000]" --assign new_coins --transfer-objects "[new_coins]" @{{address}}`

- 将一个对象转移到地址：

`sui client ptb --transfer-objects "[{{object_id}}]" @{{address}}`

- 发布一个 Move 包，并将升级能力转移给发送者：

`sui client ptb --move-call sui::tx_context::sender --assign sender --publish "." --assign upgrade_cap --transfer-objects "[upgrade_cap]" sender`
