# grub2-mkpasswd-pbkdf2

> 为 GRUB 生成哈希密码。
> 更多信息：<https://manned.org/grub2-mkpasswd-pbkdf2>.

- 使用 PBKDF2 为 GRUB 2 创建密码哈希，并将其打印到 `stdout`：

`sudo grub2-mkpasswd-pbkdf2 {{[-c|--iteration-count]}} {{number_of_pbkdf2_iterations}} {{[-s|--salt]}} {{salt_length}}`