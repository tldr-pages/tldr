# slmgr.vbs

> 安装、激活和管理 Windows 许可证。
> 此命令可能会覆盖、停用和/或删除您当前的 Windows 许可证，请谨慎操作。
> 更多信息：<https://learn.microsoft.com/windows-server/get-started/activation-slmgr-vbs-options>.

- [d]显示当前 Windows [l]许可 [i]信息：

`slmgr.vbs /dli`

- [d]显示当前设备的安装[t] [i]D。对于离线许可激活很有用：

`slmgr.vbs /dti`

- 显示当前许可证的过期[x] [r]日期和时间：

`slmgr.vbs /xpr`

- [i]安装新的 Windows 许可证 [p]roduct [k]ey。需要管理员权限，并将覆盖现有许可证：

`slmgr.vbs /ipk {{product_key}}`

- [a]在线[t]激活 Windows 产品许可证 [o]。需要管理员权限：

`slmgr.vbs /ato`

- [a]离线[t]激活 Windows [p]roduct 许可证。需要管理员权限和由 Microsoft Product Activation Center 提供的确认 ID：

`slmgr.vbs /atp {{confirmation_id}}`

- [c]从 Windows 注册表中清除当前许可证的 [p]roduct [k]ey。这不会停用或卸载当前许可证，但可以防止将来被恶意程序盗用：

`slmgr.vbs /cpky`

- [u]通过[p]roduct [k]ey卸载当前许可证：

`slmgr.vbs /upk`
