# slmgr.vbs

> 安装、激活和管理 Windows 许可证。
> 此命令可能会覆盖、停用和/或删除您当前的 Windows 许可证。请谨慎操作。
> 更多信息：<https://learn.microsoft.com/windows-server/get-started/activation-slmgr-vbs-options>。

- [d]isplay 显示当前 Windows [l]icense 许可证 [i]nformation 信息：

`slmgr.vbs /dli`

- [d]isplay 显示当前设备的 [i]nstallation 安装 [i]D ID。适用于离线许可证激活：

`slmgr.vbs /dti`

- 显示当前许可证的 e[xp]i[r]ation 过期日期和时间：

`slmgr.vbs /xpr`

- [i]nstall 安装新的 Windows 许可证 [p]roduct 产品 [k]ey 密钥。需要管理员权限，并将覆盖现有许可证：

`slmgr.vbs /ipk {{product_key}}`

- [a]c[t]ivate 激活 Windows 产品许可证 [o]nline 在线。需要管理员权限：

`slmgr.vbs /ato`

- [a]c[t]ivate 激活 Windows [p]roduct 产品许可证离线。需要管理员权限和微软产品激活中心提供的确认 ID：

`slmgr.vbs /atp {{confirmation_id}}`

- [c]lear 清除当前许可证的 [p]roduct 产品 [k]e[y] 密钥从 Windows 注册表。此操作不会停用或卸载当前许可证，但可以防止未来恶意程序窃取密钥：

`slmgr.vbs /cpky`

- [u]ninstall 卸载当前许可证（按其 [p]roduct 产品 [k]ey 密钥）：

`slmgr.vbs /upk`