# dmidecode

> 以人类可读的格式显示 DMI（也称为 SMBIOS）表内容。
> 需要 root 权限。
> 更多信息：<https://manned.org/dmidecode>.

- 显示所有 DMI 表内容：

`sudo dmidecode`

- 显示 BIOS 版本：

`sudo dmidecode -s bios-version`

- 显示系统的序列号：

`sudo dmidecode -s system-serial-number`

- 显示 BIOS 信息：

`sudo dmidecode -t bios`

- 显示 CPU 信息：

`sudo dmidecode -t processor`

- 显示内存信息：

`sudo dmidecode -t memory`
