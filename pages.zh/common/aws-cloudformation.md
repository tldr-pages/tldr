# AWS CloudFormation

> 通过将基础设施视为代码来建模、配置和管理 AWS 及第三方资源。
> 更多信息请访问：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html>。

- 从模板文件创建堆栈：

`aws cloudformation create-stack --stack-name {{stack-name}} --region {{region}} --template-body {{file://path/to/file.yml}} --profile {{profile}}`

- 删除堆栈：

`aws cloudformation delete-stack --stack-name {{stack-name}} --profile {{profile}}`

- 列出所有堆栈：

`aws cloudformation list-stacks --profile {{profile}}`

- 列出所有运行中的堆栈：

`aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE --profile {{profile}}`

- 检查堆栈状态：

`aws cloudformation describe-stacks --stack-name {{stack-id}} --profile {{profile}}`

- 启动堆栈漂移检测：

`aws cloudformation detect-stack-drift --stack-name {{stack-id}} --profile {{profile}}`

- 使用前一个命令输出中的 'StackDriftDetectionId' 检查堆栈的漂移状态输出：

`aws cloudformation describe-stack-resource-drifts --stack-name {{stack-drift-detection-id}} --profile {{profile}}`