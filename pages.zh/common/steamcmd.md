# steamcmd

> Steam 客户端的命令行版本。
> 更多信息：<https://manned.org/steamcmd>。

- 匿名安装或更新应用程序：

`steamcmd +login {{anonymous}} +app_update {{appid}} +quit`

- 使用指定的凭据安装或更新应用程序：

`steamcmd +login {{username}} +app_update {{appid}} +quit`

- 为特定平台安装应用程序：

`steamcmd +@sSteamCmdForcePlatformType {{windows}} +login {{anonymous}} +app_update {{appid}} validate +quit`