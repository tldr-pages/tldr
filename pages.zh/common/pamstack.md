# pamstack

> 将多个 PAM 图像的平面堆叠成一个 PAM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamstack.html>.

- 按指定顺序堆叠指定的 PAM 图像的平面：

`pamstack {{path/to/image1.pam path/to/image2.pam ...}} > {{path/to/output.pam}}`

- 指定输出 PAM 文件的元组类型名称（最多 255 个字符）：

`pamstack -tupletype {{tuple_type}} {{path/to/image1.pam path/to/image2.pam ...}} > {{path/to/output.pam}}`