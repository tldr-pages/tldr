# blkpr

> 在支持持久保留的块设备上注册、保留、释放、抢占和清除持久保留。
> 更多信息：<https://manned.org/blkpr>。

- 在给定设备上使用指定的密钥注册（命令）新的保留：

`blkpr {{-c|--command}} register {{-k|--key}} {{reservation_key}} {{path/to/device}}`

- 将现有保留的类型设置为独占访问：

`blkpr -c reserve {{-k|--key}} {{reservation_key}} {{-t|--type}} exclusive-access {{path/to/device}}`

- 用给定的密钥抢占现有保留，并用新保留替换它：

`blkpr -c preempt {{-K|--oldkey}} {{old_key}} {{-k|--key}} {{new_key}} {{-t|--type}} write-exclusive {{path/to/device}}`

- 在给定设备上释放具有指定密钥和类型的保留：

`blkpr -c release {{-k|--key}} {{reservation_key}} {{-t|--type}} {{reservation_type}} {{path/to/device}}`

- 从给定设备中清除所有保留：

`blkpr -c clear {{-k|--key}} {{key}} {{path/to/device}}`