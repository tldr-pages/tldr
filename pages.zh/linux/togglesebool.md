# togglesebool

> 翻转当前（非持久）SELinux 布尔值。
> 注意：此工具已被弃用，通常被 `setsebool` 替代。
> 更多信息：<https://manned.org/togglesebool>。

- 翻转指定布尔值的当前（非持久）值：

`sudo togglesebool {{virt_use_samba virt_use_usb ...}}`