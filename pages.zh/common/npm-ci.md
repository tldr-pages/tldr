# npm ci

> 用于自动化环境的 `npm` 项目依赖的清洁安装。
> 基于 `package-lock.json` 或 `npm-shrinkwrap.json` 安装包。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-ci>。

- 从 `package-lock.json` 或 `npm-shrinkwrap.json` 安装项目依赖：

`npm ci`

- 安装项目依赖，但跳过指定的依赖类型：

`npm ci --omit={{dev|optional|peer}}`

- 安装项目依赖，不运行 `package.json` 中定义的任何预/后脚本：

`npm ci --ignore-scripts`
