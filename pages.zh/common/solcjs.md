# solcjs

> 一组用于Solidity编译器的JavaScript绑定。
> 更多信息：<https://github.com/ethereum/solc-js>。

- 将特定合约编译为十六进制：

`solcjs --bin {{path/to/file.sol}}`

- 编译特定合约的ABI：

`solcjs --abi {{path/to/file.sol}}`

- 指定一个基本路径以解析导入：

`solcjs --bin --base-path {{path/to/directory}} {{path/to/file.sol}}`

- 指定一个或多个包含外部代码的路径：

`solcjs --bin --include-path {{path/to/directory}} {{path/to/file.sol}}`

- 优化生成的字节码：

`solcjs --bin --optimize {{path/to/file.sol}}`