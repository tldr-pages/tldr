# npm find-dupes

> 识别 `node_modules` 中的重复依赖。
> 更多信息: <https://docs.npmjs.com/cli/commands/npm-find-dupes>。

- 列出 `node_modules` 中的所有重复包：

`npm find-dupes`

- 在重复检测中包括 `devDependencies`：

`npm find-dupes --include=dev`

- 列出 `node-modules` 中特定包的所有重复实例：

`npm find-dupes {{package_name}}`

- 从重复检测中排除可选依赖：

`npm find-dupes --omit=optional`

- 设置输出的日志级别：

`npm find-dupes --loglevel={{silent|error|warn|info|verbose}}`

- 以 JSON 格式输出重复信息：

`npm find-dupes --json`

- 将重复搜索限制在特定范围内：

`npm find-dupes --scope={{@scope1,@scope2}}`

- 从重复检测中排除特定范围：

`npm find-dupes --omit-scope={{@scope1,@scope2}}`