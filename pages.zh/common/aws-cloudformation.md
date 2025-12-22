# aws cloudformation

> 通过将基础设施视为代码来建模、预置和管理 AWS 以及第三方资源。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/cloudformation/>.

- 从模板文件创建一个堆栈：

`aws cloudformation create-stack --stack-name {{堆栈名称}} --region {{区域}} --template-body {{file://路径/到/文件.yml}} --profile {{配置文件}}`

- 删除一个堆栈：

`aws cloudformation delete-stack --stack-name {{堆栈名称}} --profile {{配置文件}}`

- 列出所有堆栈：

`aws cloudformation list-stacks --profile {{配置文件}}`

- 列出所有正在运行的堆栈：

`aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE --profile {{配置文件}}`

- 检查一个堆栈的状态：

`aws cloudformation describe-stacks --stack-name {{堆栈 ID}} --profile {{配置文件}}`

- 为一个堆栈启动漂移检测：

`aws cloudformation detect-stack-drift --stack-name {{堆栈 ID}} --profile {{配置文件}}`

- 使用前一个命令输出中的 `StackDriftDetectionId` 检查堆栈的漂移状态输出：

`aws cloudformation describe-stack-resource-drifts --stack-name {{堆栈漂移检测 ID}} --profile {{配置文件}}`
