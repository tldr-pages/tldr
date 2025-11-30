# kubectl cp

> Copy files and directories between a local filesystem and a container in a pod.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cp/>.

- Copy a local file or directory to a pod:

`kubectl cp {{local_path}} {{pod_name}}:{{container_path}}`

- Copy a local file to a pod in a specific namespace:

`kubectl cp {{local_path}} {{namespace}}/{{pod_name}}:{{container_path}}`

- Copy a file from a pod to the local machine:

`kubectl cp {{namespace}}/{{pod_name}}:{{container_file}} {{local_path}}`

- Copy a file to a specific container in a pod:

`kubectl cp {{local_path}} {{pod_name}}:{{container_path}} {{[-c|--container]}} {{container_name}}`

- Copy a file to a pod without preserving ownership and permissions:

`kubectl cp {{local_path}} {{namespace}}/{{pod_name}}:{{container_file}} --no-preserve`
