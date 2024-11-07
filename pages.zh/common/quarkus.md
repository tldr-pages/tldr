# quarkus

> 创建 Quarkus 项目，管理扩展并执行基本的构建和开发任务。
> 更多信息：<https://quarkus.io/guides/cli-tooling>.

- 在一个新目录中创建一个新的应用程序项目：

`quarkus create app {{项目名称}}`

- 在实时编码模式下运行当前项目：

`quarkus dev`

- 运行应用程序：

`quarkus run`

- 在连续测试模式下运行当前项目：

`quarkus test`

- 向当前项目添加一个或多个扩展：

`quarkus extension add {{扩展名1 扩展名2 ...}}`

- 使用 Docker 构建容器镜像：

`quarkus image build docker`

- 将应用程序部署到 Kubernetes：

`quarkus deploy kubernetes`

- 更新项目：

`quarkus update`
