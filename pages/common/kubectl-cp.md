# kubectl cp

> Copy files and directories between a local filesystem and a container in a pod.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cp/>.

- Copy a local file or directory to a pod:

`kubectl cp {{path/to/local_file}} {{pod_name}}:{{/path/to/file_in_pod}}`

- Copy a local file or directory to a pod in a specific namespace:

`kubectl cp {{path/to/local_file}} {{namespace}}/{{pod_name}}:{{/path/to/file_in_pod}}`

- Copy a file or directory from a pod to the local machine:

`kubectl cp {{namespace}}/{{pod_name}}:{{/path/to/file_in_pod}} {{path/to/local_file}}`

- Copy a file or directory to a specific container in a pod:

`kubectl cp {{path/to/local_file}} {{pod_name}}:{{/path/to/file_in_pod}} {{[-c|--container]}} {{container_name}}`

- Copy a file or directory to a pod without preserving ownership and permissions:

`kubectl cp {{path/to/local_file}} {{namespace}}/{{pod_name}}:{{/path/to/file_in_pod}} --no-preserve`

- Copy a local file or directory to a pod with retries on failure:

`kubectl cp {{path/to/local_file}} {{pod_name}}:{{/path/to/file_in_pod}} --retries {{3}}`
