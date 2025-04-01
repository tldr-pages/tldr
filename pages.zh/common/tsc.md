# tsc

> TypeScript 编译器。
> 更多信息：<https://www.typescriptlang.org/docs/handbook/compiler-options.html>。

- 将 TypeScript 文件 `foobar.ts` 编译为 JavaScript 文件 `foobar.js`：

`tsc {{foobar.ts}}`

- 使用特定的目标语法（默认为 `ES3`）将 TypeScript 文件编译为 JavaScript：

`tsc --target {{ES5|ES2015|ES2016|ES2017|ES2018|ESNEXT}} {{foobar.ts}}`

- 将 TypeScript 文件编译为具有自定义名称的 JavaScript 文件：

`tsc --outFile {{output.js}} {{input.ts}}`

- 编译 `tsconfig.json` 文件中定义的所有 `.ts` 文件：

`tsc --build {{tsconfig.json}}`

- 从文本文件中读取命令行选项和参数来运行编译器：

`tsc @{{args.txt}}`

- 对多个 JavaScript 文件进行类型检查，并仅输出错误：

`tsc --allowJs --checkJs --noEmit {{src/**/*.js}}`

- 以监控模式运行编译器，当代码发生变化时自动重新编译：

`tsc --watch`
