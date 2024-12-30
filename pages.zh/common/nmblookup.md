# nmblookup

> 发现 SMB 共享。
> 更多信息：<https://www.samba.org/samba/docs/current/man-html/nmblookup.1.html>。

- 查找本地网络中具有 SMB 共享的主机：

`nmblookup -S '*'`

- 查找本地网络中由 SAMBA 运行的 SMB 共享的主机：

`nmblookup --status __SAMBA__`