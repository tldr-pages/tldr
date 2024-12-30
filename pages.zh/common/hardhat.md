# hardhat

> 以太坊软件的开发环境。
> 更多信息：<https://hardhat.org>。

- 列出可用的子命令（如果没有配置，则创建一个新项目）：

`hardhat`

- 编译当前项目并构建所有工件：

`hardhat compile`

- 在编译项目后运行用户定义的脚本：

`hardhat run {{path/to/script.js}}`

- 运行 Mocha 测试：

`hardhat test`

- 运行所有给定的测试文件：

`hardhat test {{path/to/file1.js}} {{path/to/file2.js}}`

- 启动一个本地以太坊 JSON-RPC 节点进行开发：

`hardhat node`

- 启动一个具有特定主机名和端口的本地以太坊 JSON-RPC 节点：

`hardhat node --hostname {{hostname}} --port {{port}}`

- 清理缓存和所有工件：

`hardhat clean`