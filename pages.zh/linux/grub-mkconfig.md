# grub-mkconfig

> 生成一个 GRUB 配置文件。
> 更多信息：<https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dmkconfig.html>。

- 进行干运行并将配置打印到 `stdout`：

`sudo grub-mkconfig`

- 生成配置文件：

`sudo grub-mkconfig --output={{/boot/grub/grub.cfg}}`

- 显示帮助：

`grub-mkconfig --help`