# minikube սկիզբ

> Սկսեք `minikube`-ը տարբեր կոնֆիգուրացիաներով:.
> Լրացուցիչ տեղեկություններ. <https://minikube.sigs.k8s.io/docs/commands/start/>:.

- Սկսեք `minikube`-ը Kubernetes-ի կոնկրետ տարբերակով.:

`minikube start --kubernetes-version {{v1.24.0}}`

- Սկսեք `minikube`-ը որոշակի ռեսուրսների հատկացումներով (օրինակ՝ հիշողություն և պրոցեսոր):

`minikube start --memory {{2048}} --cpus {{2}}`

- Սկսեք `minikube`-ը կոնկրետ դրայվերով (օրինակ՝ VirtualBox):

`minikube start --driver {{virtualbox}}`

- Սկսեք `minikube`-ը հետին պլանում (անգլուխ ռեժիմ).:

`minikube start --background`

- Սկսեք `minikube`-ը հատուկ հավելումներով (օրինակ՝ չափման սերվերով).:

`minikube start --addons {{metrics-server}}`
