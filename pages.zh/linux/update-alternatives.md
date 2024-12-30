# 更新替代方案

> 方便地维护符号链接以确定默认命令。
> 更多信息：<https://manned.org/update-alternatives>。

- 添加符号链接：

`sudo update-alternatives --install {{符号链接的路径}} {{命令名称}} {{命令二进制文件的路径}} {{优先级}}`

- 配置`java`的符号链接：

`sudo update-alternatives --config {{java}}`

- 移除符号链接：

`sudo update-alternatives --remove {{java}} {{/opt/java/jdk1.8.0_102/bin/java}}`

- 显示关于指定命令的信息：

`update-alternatives --display {{java}}`

- 显示所有命令及其当前选择：

`update-alternatives --get-selections`