# rage

> 一个简单、安全、现代的文件加密工具（以及 Rust 库），具有小的显式密钥，没有配置选项，并具备 UNIX 风格的组合性。
> `age` 的 Rust 实现。
> 更多信息请访问：<https://github.com/str4d/rage>。

- 为 `user` 加密一个文件并将其保存为 `message.age`：

`echo "{{您的秘密消息}}" | rage --encrypt --recipient {{user}} --output {{path/to/message.age}}`

- 使用 `identity_file` 解密一个文件并将其保存为 `message`：

`rage --decrypt --identity {{path/to/identity_file}} --output {{message}}`