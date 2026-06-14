# minikube

> Գործարկեք Kubernetes-ը տեղական մակարդակում:.
> Լրացուցիչ տեղեկություններ. <https://minikube.sigs.k8s.io/docs/>:.

- Սկսեք կլաստերը.:

`minikube start`

- Ստացեք կլաստերի IP հասցեն.:

`minikube ip`

- Մուտք գործեք `my_service` անունով ծառայություն, որը բացահայտված է հանգույցի միացքի միջոցով և ստացեք URL-ը.:

`minikube service {{my_service}} --url`

- Բացեք Kubernetes վահանակը զննարկիչում.:

`minikube dashboard`

- Դադարեցրեք վազող կլաստերը.:

`minikube stop`

- Ջնջել կլաստերը.:

`minikube delete`

- Միացեք LoadBalancer ծառայություններին.:

`minikube tunnel`
