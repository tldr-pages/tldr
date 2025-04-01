# nmblookup

> 发现 SMB 共享。
> 更多信息：<https://www.samba.org/samba/docs/current/man-html/nmblookup.1.html>.

- 在本地网络中查找具有 SMB 共享的主机：

`nmblookup -S '*'`

- 在本地网络中查找由 SAMBA 运行的 SMB 共享主机：

`nmblookup --status __SAMBA__`