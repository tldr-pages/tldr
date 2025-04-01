# minifab

> 自动化设置和部署 Hyperledger Fabric 网络。
> 更多信息：<https://github.com/hyperledger-labs/minifabric>.

- 启动默认的 Hyperledger Fabric 网络：

`minifab up -i {{minifab_version}}`

- 关闭 Hyperledger Fabric 网络：

`minifab down`

- 在指定的通道上安装链码：

`minifab install -n {{chaincode_name}}`

- 在通道上安装特定版本的链码：

`minifab install -n {{chaincode_name}} -v {{chaincode_version}}`

- 安装/升级链码后进行初始化：

`minifab approve,commit,initialize,discover`

- 使用指定参数调用链码方法：

`minifab invoke -n {{chaincode_name}} -p '"{{method_name}}", "{{argument1}}", "{{argument2}}", ...'`

- 查询账本：

`minifab blockquery {{block_number}}`

- 快速运行应用程序：

`minifab apprun -l {{app_programming_language}}`
