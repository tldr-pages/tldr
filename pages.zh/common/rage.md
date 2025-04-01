# rage

> 一个简单、安全且现代的文件加密工具（也是 Rust 库），具有小巧显式的密钥、无配置选项和 UNIX 风格的组合性。
> `age` 的 Rust 实现。
> 更多信息：<https://github.com/str4d/rage>。

- 为 `user` 加密文件并保存为 `message.age`：

`echo "{{您的秘密信息}}" | rage --encrypt --recipient {{user}} --output {{path/to/message.age}}`

- 使用 `identity_file` 解密文件并保存为 `message`：

`rage --decrypt --identity {{path/to/identity_file}} --output {{message}}`