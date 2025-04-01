# blkpr

> 在支持持久预留的块设备上注册、预留、释放、抢占和清除持久预留。
> 更多信息：<https://manned.org/blkpr>.

- 使用给定的密钥在指定设备上注册新的预留：

`blkpr {{[-c|--command]}} register {{[-k|--key]}} {{reservation_key}} {{path/to/device}}`

- 将现有预留的类型设置为独占访问：

`blkpr {{[-c|--command]}} reserve {{[-k|--key]}} {{reservation_key}} {{[-t|--type]}} exclusive-access {{path/to/device}}`

- 使用给定的旧密钥抢占现有预留，并用新的预留替换它：

`blkpr {{[-c|--command]}} preempt {{[-K|--oldkey]}} {{old_key}} {{[-k|--key]}} {{new_key}} {{[-t|--type]}} write-exclusive {{path/to/device}}`

- 释放指定设备上具有给定密钥和类型的预留：

`blkpr {{[-c|--command]}} release {{[-k|--key]}} {{reservation_key}} {{[-t|--type]}} {{reservation_type}} {{path/to/device}}`

- 清除指定设备上的所有预留：

`blkpr {{[-c|--command]}} clear {{[-k|--key]}} {{key}} {{path/to/device}}`
