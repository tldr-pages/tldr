# kubeadm

> Interfaz de línea de comandos para crear y gestionar clusters Kubernetes.
> Más información: <https://kubernetes.io/docs/reference/setup-tools/kubeadm>.

- Crea un plano de control de Kubernetes:

`kubeadm init`

- Arranca un nodo trabajador de Kubernetes y lo une a un clúster:

`kubeadm join --token {{token}}`

- Crea un nuevo token de arranque con un TTL de 12 horas:

`kubeadm token create --ttl {{12h0m0s}}`

- Comprueba si el clúster Kubernetes es actualizable y qué versiones están disponibles:

`kubeadm upgrade plan`

- Actualiza el clúster Kubernetes a la versión especificada:

`kubeadm upgrade apply {{versión}}`

- Observa el ConfigMap de kubeadm que contiene la configuración del clúster:

`kubeadm config view`

- Revierte los cambios realizados en el host por `kubeadm init` o `kubeadm join`:

`kubeadm reset`
