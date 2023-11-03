# xctool

> 用于构建 Xcode 项目的工具。
> 更多信息：<https://github.com/facebookarchive/xctool>.

- 在没有任何工作区的情况下生成单个项目：

`xctool -project {{你的项目.名称}} -scheme {{方案}} build`

- 构建属于工作区的项目：

`xctool -workspace {{你的工作区.名字}} -scheme {{方案}} build`

- 清理、构建和执行所有测试：

`xctool -workspace {{你的工作区.名字}} -scheme {{方案}} clean build test`
