# dmidecode

> 以人类可读的格式显示 DMI（也称为 SMBIOS）表内容。
> 需要 root 权限。
> 另请参阅：`inxi`, `lshw`, `hwinfo`。
> 更多信息：<https://manned.org/dmidecode>。

- 显示所有 DMI 表内容：

`sudo dmidecode`

- 显示 BIOS 版本：

`sudo dmidecode {{[-s|--string]}} bios-version`

- 显示系统的序列号：

`sudo dmidecode {{[-s|--string]}} system-serial-number`

- 显示 BIOS 信息：

`sudo dmidecode {{[-t|--type]}} bios`

- 显示 CPU 信息：

`sudo dmidecode {{[-t|--type]}} processor`

- 显示内存信息：

`sudo dmidecode {{[-t|--type]}} memory`
