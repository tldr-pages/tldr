# hostnamectl

> 获取或设置计算机的主机名。
> 更多信息：<https://manned.org/hostnamectl>。

- 获取计算机的主机名：

`hostnamectl`

- 设置计算机的主机名：

`sudo hostnamectl set-hostname "{{hostname}}"`

- 为计算机设置一个友好的主机名：

`sudo hostnamectl set-hostname --static "{{hostname.example.com}}" && sudo hostnamectl set-hostname --pretty "{{hostname}}"`

- 将主机名重置为默认值：

`sudo hostnamectl set-hostname --pretty ""`