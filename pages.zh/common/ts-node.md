# ts-node

> 直接运行 TypeScript 代码，无需编译。
> 更多信息：<https://typestrong.org/ts-node>.

- 执行 TypeScript 文件，不进行编译（`node` + `tsc`）：

`ts-node {{path/to/file.ts}}`

- 执行 TypeScript 文件，不加载 `tsconfig.json`：

`ts-node --skip-project {{path/to/file.ts}}`

- 评估作为字面量传递的 TypeScript 代码：

`ts-node --eval '{{console.log("Hello World")}}'`

- 以脚本模式执行 TypeScript 文件：

`ts-node --script-mode {{path/to/file.ts}}`

- 将 TypeScript 文件转译为 JavaScript 而不执行：

`ts-node --transpile-only {{path/to/file.ts}}`

- 显示 TS-Node 帮助：

`ts-node --help`
