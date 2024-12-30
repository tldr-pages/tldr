# gcloud 组件安装

> 安装 Google Cloud CLI 的组件及其依赖项。
> 在不升级现有安装的情况下，安装当前版本的 Google Cloud CLI 组件。
> 更多信息：<https://cloud.google.com/sdk/gcloud/reference/components/install>。

- 查看可安装的组件：

`gcloud components list`

- 安装一个或多个组件（同时安装任何依赖项）：

`gcloud components install {{component_id1 component_id2 ...}}`

- 检查当前版本的 Google Cloud CLI：

`gcloud version`

- 将 Google Cloud CLI 更新到最新版本：

`gcloud components update`