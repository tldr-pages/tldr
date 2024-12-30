# warp-diag

> Cloudflare WARP 服务的诊断和反馈工具。
> 另见：`warp-cli`。
> 更多信息：<https://developers.cloudflare.com/warp-client/>。

- 生成一个包含系统配置和 WARP 连接信息的 Zip 文件：

`warp-diag`

- 生成一个包含调试信息的 Zip 文件，并在输出文件名中添加时间戳：

`warp-diag --add-ts`

- 将输出文件保存在特定目录下：

`warp-diag --output {{path/to/directory}}`

- 以交互方式向 Cloudflare 的 WARP 提交新的反馈：

`warp-diag feedback`