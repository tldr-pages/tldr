# solcjs

> 一组用于 Solidity 编译器的 JavaScript 绑定。
> 更多信息：<https://github.com/ethereum/solc-js>。

- 编译特定合约为十六进制：

`solcjs --bin {{path/to/file.sol}}`

- 编译特定合约的 ABI：

`solcjs --abi {{path/to/file.sol}}`

- 指定一个基本路径以解析导入文件：

`solcjs --bin --base-path {{path/to/directory}} {{path/to/file.sol}}`

- 指定一个或多个包含外部代码的路径：

`solcjs --bin --include-path {{path/to/directory}} {{path/to/file.sol}}`

- 优化生成的字节码：

`solcjs --bin --optimize {{path/to/file.sol}}`