# apt-key

> APT 包管理器的密钥管理工具，适用于 Debian 和 Ubuntu。
> 注意：`apt-key` 现在已被弃用（维护脚本中使用 `apt-key del` 的情况除外）。
> 更多信息：<https://manned.org/apt-key.8>。

- 列出受信任的密钥：

`apt-key list`

- 将密钥添加到受信任的密钥库：

`apt-key add {{public_key_file.asc}}`

- 从受信任的密钥库中删除密钥：

`apt-key del {{key_id}}`

- 将远程密钥添加到受信任的密钥库：

`wget -qO - {{https://host.tld/filename.key}} | apt-key add -`

- 仅使用密钥 ID 从密钥服务器添加密钥：

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{KEYID}}`