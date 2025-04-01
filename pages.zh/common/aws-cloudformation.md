# aws cloudformation

> 通过将基础设施作为代码来建模、配置和管理 AWS 和第三方资源。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html>.

- 从模板文件创建堆栈：

`aws cloudformation create-stack --stack-name {{stack-name}} --region {{region}} --template-body {{file://path/to/file.yml}} --profile {{profile}}`

- 删除堆栈：

`aws cloudformation delete-stack --stack-name {{stack-name}} --profile {{profile}}`

- 列出所有堆栈：

`aws cloudformation list-stacks --profile {{profile}}`

- 列出所有正在运行的堆栈：

`aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE --profile {{profile}}`

- 查看堆栈的状态：

`aws cloudformation describe-stacks --stack-name {{stack-id}} --profile {{profile}}`

- 开始检测堆栈的偏差：

`aws cloudformation detect-stack-drift --stack-name {{stack-id}} --profile {{profile}}`

- 使用上一个命令输出的 'StackDriftDetectionId' 查看堆栈的偏差状态输出：

`aws cloudformation describe-stack-resource-drifts --stack-name {{stack-drift-detection-id}} --profile {{profile}}`