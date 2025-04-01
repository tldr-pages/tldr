# npm dedupe

> 减少 `node_modules` 目录中的重复项。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-dedupe>。

- 减少 `node_modules` 中的包重复：

`npm dedupe`

- 在去重过程中遵循 `package-lock.json` 或 `npm-shrinkwrap.json`：

`npm dedupe --lock`

- 以严格模式运行去重：

`npm dedupe --strict`

- 在去重过程中跳过可选/对等依赖：

`npm dedupe --omit={{optional|peer}}`

- 启用详细日志以便于故障排除：

`npm dedupe --loglevel=verbose`

- 仅对特定包进行去重：

`npm dedupe {{package_name}}`