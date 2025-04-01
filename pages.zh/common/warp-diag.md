# warp-diag

> Cloudflare 的 WARP 服务的诊断和反馈工具。
> 另请参阅：`warp-cli`。
> 更多信息：<https://developers.cloudflare.com/warp-client/>。

- 生成包含系统配置和 WARP 连接信息的 Zip 文件：

`warp-diag`

- 生成包含调试信息的 Zip 文件，并在输出文件名中添加时间戳：

`warp-diag --add-ts`

- 将输出文件保存到指定目录：

`warp-diag --output {{path/to/directory}}`

- 与 Cloudflare 的 WARP 交互式提交新反馈：

`warp-diag feedback`