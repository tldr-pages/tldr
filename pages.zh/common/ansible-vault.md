# ansible-vault

> 在 Ansible 项目中对值、数据结构和文件进行加密和解密。
> 更多信息：<https://docs.ansible.com/projects/ansible/latest/vault_guide/index.html>.

- 创建一个新的加密保管库文件，并提示输入密码：

`ansible-vault create {{保管库文件}}`

- 使用保管库密码文件创建一个新的加密保管库文件：

`ansible-vault create --vault-password-file {{密码文件}} {{保管库文件}}`

- 使用可选的密码文件加密一个已有文件：

`ansible-vault encrypt --vault-password-file {{密码文件}} {{保管库文件}}`

- 使用 Ansible 的加密字符串格式加密一个字符串，并显示交互式提示：

`ansible-vault encrypt_string`

- 查看一个加密文件，并使用密码文件进行解密：

`ansible-vault view --vault-password-file {{密码文件}} {{保管库文件}}`

- 使用新的密码文件为已加密的保管库文件重新设置密钥：

`ansible-vault rekey --vault-password-file {{旧密码文件}} --new-vault-password-file {{新密码文件}} {{保管库文件}}`
