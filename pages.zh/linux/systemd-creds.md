# systemd-creds

> 列出、显示、加密和解密服务凭证。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-creds.html>.

- 加密文件并设置特定名称：

`systemd-creds encrypt --name={{name}} {{path/to/input_file}} {{path/to/output}}`

- 再次解密文件：

`systemd-creds decrypt {{path/to/input_file}} {{path/to/output_file}}`

- 从 `stdin` 加密文本：

`echo -n {{text}} | systemd-creds encrypt --name={{name}} - {{path/to/output}}`

- 加密文本并将其追加到服务文件（凭证将在 `$CREDENTIALS_DIRECTORY` 中可用）：

`echo -n {{text}} | systemd-creds encrypt --name={{name}} --pretty - - >> {{service}}`

- 创建仅在给定时间戳之前有效的凭证：

`systemd-creds encrypt --not-after="{{timestamp}}" {{path/to/input_file}} {{path/to/output_file}}`