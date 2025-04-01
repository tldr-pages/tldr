# oc

> OpenShift 容器平台命令行工具。
> 用于应用程序和容器的管理。
> 更多信息：<https://docs.openshift.com/container-platform/3.11/cli_reference/get_started_cli.html>。

- 登录到 OpenShift 容器平台服务器：

`oc login`

- 创建新项目：

`oc new-project {{project_name}}`

- 切换到现有项目：

`oc project {{project_name}}`

- 向项目中添加新应用：

`oc new-app {{repo_url}} --name {{application}}`

- 打开到容器的远程 shell 会话：

`oc rsh {{pod_name}}`

- 列出项目中的 Pod：

`oc get pods`

- 从当前会话登出：

`oc logout`