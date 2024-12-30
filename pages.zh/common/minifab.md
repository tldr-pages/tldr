# minifab

> 自动化设置和部署 Hyperledger Fabric 网络。
> 更多信息：<https://github.com/hyperledger-labs/minifabric>。

- 启动默认的 Hyperledger Fabric 网络：

`minifab up -i {{minifab_version}}`

- 停止 Hyperledger Fabric 网络：

`minifab down`

- 在指定的通道上安装链码：

`minifab install -n {{chaincode_name}}`

- 在通道上安装特定的链码版本：

`minifab install -n {{chaincode_name}} -v {{chaincode_version}}`

- 在安装/升级后初始化链码：

`minifab approve,commit,initialize,discover`

- 使用指定的参数调用链码方法：

`minifab invoke -n {{chaincode_name}} -p '"{{method_name}}", "{{argument1}}", "{{argument2}}", ...'`

- 对账本进行查询：

`minifab blockquery {{block_number}}`

- 快速运行一个应用程序：

`minifab apprun -l {{app_programming_language}}`