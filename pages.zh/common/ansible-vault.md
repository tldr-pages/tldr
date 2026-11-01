# ansible-vault

> 加密和解密 Ansible 项目中的值、数据结构和文件。
> 更多信息：<https://docs.ansible.com/projects/ansible/latest/vault_guide/index.html>。

- 通过交互式密码提示创建新的加密保险库文件：

`ansible-vault create {{路径/到/保险库_文件}}`

- 通过交互式密码提示编辑、查看或重新生成密钥（重新加密）现有的加密保险库文件：

`ansible-vault {{edit|view|rekey}} {{路径/到/保险库_文件}}`

- 使用密码文件创建新的加密保险库文件：

`ansible-vault create --vault-password-file {{路径/到/密码_文件}} {{路径/到/保险库_文件}}`

- 使用密码文件原地加密现有的明文文件：

`ansible-vault encrypt --vault-password-file {{路径/到/密码_文件}} {{路径/到/文件}}`

- 使用 Ansible 的加密字符串格式加密字符串，并进行交互式密码提示：

`ansible-vault encrypt_string`

- 使用密码文件解密并查看加密的保险库文件：

`ansible-vault view --vault-password-file {{路径/到/密码_文件}} {{路径/到/保险库_文件}}`

- 使用新的密码文件为已加密的保险库文件重新生成密钥（重新加密）：

`ansible-vault rekey --vault-password-file {{路径/到/旧_密码_文件}} --new-vault-password-file {{路径/到/新_密码_文件}} {{路径/到/保险库_文件}}`
