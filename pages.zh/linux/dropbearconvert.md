# dropbearconvert

> 在 Dropbear 和 OpenSSH 私钥格式之间进行转换。
> 更多信息：<https://manned.org/dropbearconvert.1>.

- 将 OpenSSH 私钥转换为 Dropbear 格式：

`dropbearconvert openssh dropbear {{path/to/input_key}} {{path/to/output_key}}`

- 将 Dropbear 私钥转换为 OpenSSH 格式：

`dropbearconvert dropbear openssh {{path/to/input_key}} {{path/to/output_key}}`
