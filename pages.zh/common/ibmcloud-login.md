# ibmcloud 登录

> 登录到 IBM Cloud。
> 更多信息：<https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login>。

- 使用交互式提示登录：

`ibmcloud login`

- 登录到特定的 API 端点（默认是 `cloud.ibm.com`）：

`ibmcloud login -a {{api_endpoint}}`

- 通过提供用户名、密码和目标区域作为参数登录：

`ibmcloud login -u {{username}} -p {{password}} -r {{us-south}}`

- 使用 API 密钥登录，将其作为参数传递：

`ibmcloud login --apikey {{api_key_string}}`

- 使用 API 密钥登录，将其作为文件传递：

`ibmcloud login --apikey @{{path/to/api_key_file}}`

- 使用联邦 ID（单点登录）登录：

`ibmcloud login --sso`