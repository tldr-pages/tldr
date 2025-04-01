# pacman-key

> 用于管理 Pacman 密钥环的 GnuPG 脚本。
> 有关 `pacman` 的更多信息：<https://manned.org/pacman-key>.

- 初始化 `pacman` 密钥环：

`sudo pacman-key --init`

- 添加默认的 Arch Linux 密钥：

`sudo pacman-key --populate {{archlinux}}`

- 列出公钥环中的密钥：

`pacman-key --list-keys`

- 添加指定的密钥：

`sudo pacman-key --add {{path/to/keyfile.gpg}}`

- 从密钥服务器接收密钥：

`sudo pacman-key --recv-keys "{{uid|name|email}}"`

- 打印特定密钥的指纹：

`pacman-key --finger "{{uid|name|email}}"`

- 本地签名导入的密钥：

`sudo pacman-key --lsign-key "{{uid|name|email}}"`

- 删除特定密钥：

`sudo pacman-key --delete "{{uid|name|email}}"`
