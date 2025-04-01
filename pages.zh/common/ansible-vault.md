# ansible-vault

> 加密和解密 Ansible 项目中的值、数据结构和文件。
> 更多信息：<https://docs.ansible.com/ansible/latest/user_guide/vault.html#id17>。

- 创建一个新加密的金库文件，并提示输入密码：

`ansible-vault create {{vault_file}}`

- 使用金库密钥文件创建一个新的加密金库文件：

`ansible-vault create --vault-password-file {{password_file}} {{vault_file}}`

- 使用可选的密码文件加密现有文件：

`ansible-vault encrypt --vault-password-file {{password_file}} {{vault_file}}`

- 使用 Ansible 的加密字符串格式加密字符串，显示交互式提示：

`ansible-vault encrypt_string`

- 使用密码文件解密并查看加密文件：

`ansible-vault view --vault-password-file {{password_file}} {{vault_file}}`

- 使用新的密码文件重新加密已加密的金库文件：

`ansible-vault rekey --vault-password-file {{old_password_file}} --new-vault-password-file {{new_password_file}} {{vault_file}}`
