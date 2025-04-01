# npm find-dupes

> 在 `node_modules` 中识别重复的依赖项。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-find-dupes>.

- 列出 `node_modules` 中的所有重复包：

`npm find-dupes`

- 在检测重复包时包括 `devDependencies`：

`npm find-dupes --include=dev`

- 列出 `node_modules` 中特定包的所有重复实例：

`npm find-dupes {{package_name}}`

- 在检测重复包时排除可选依赖项：

`npm find-dupes --omit=optional`

- 设置输出的日志级别：

`npm find-dupes --loglevel={{silent|error|warn|info|verbose}}`

- 以 JSON 格式输出重复信息：

`npm find-dupes --json`

- 将重复检查限制在特定的作用域内：

`npm find-dupes --scope={{@scope1,@scope2}}`

- 在检测重复包时排除特定的作用域：

`npm find-dupes --omit-scope={{@scope1,@scope2}}`