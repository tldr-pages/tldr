# chpasswd

> 使用标准输入更改多个用户的密码。
> 更多信息：<https://manned.org/chpasswd.8>.

- 更改特定用户的密码：

`printf "{{username}}:{{new_password}}" | sudo chpasswd`

- 更改多个用户的密码（输入文本中不得包含任何空格）：

`printf "{{username_1}}:{{new_password_1}}\n{{username_2}}:{{new_password_2}}" | sudo chpasswd`

- 更改特定用户的密码，并以加密形式指定新密码：

`printf "{{username}}:{{new_encrypted_password}}" | sudo chpasswd --encrypted`

- 更改特定用户的密码，并使用特定的加密方法存储密码：

`printf "{{username}}:{{new_password}}" | sudo chpasswd --crypt-method {{NONE|DES|MD5|SHA256|SHA512}}`