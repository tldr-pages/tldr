# minikube start

> 使用不同配置启动 `minikube`。
> 更多信息：<https://minikube.sigs.k8s.io/docs/commands/start/>.

- 使用指定的 Kubernetes 版本启动 `minikube`：

`minikube start --kubernetes-version {{v1.24.0}}`

- 使用特定的资源分配（例如，内存和 CPU）启动 `minikube`：

`minikube start --memory {{2048}} --cpus {{2}}`

- 使用特定的驱动程序（例如，VirtualBox）启动 `minikube`：

`minikube start --driver {{virtualbox}}`

- 在后台启动 `minikube`（无头模式）：

`minikube start --background`

- 使用自定义插件启动 `minikube`（例如，指标服务器）：

`minikube start --addons {{metrics-server}}`