# kubectl cp

> Copy files and directories to and from containers.
> Paths are in the form `[[namespace]/]pod:container_path` when copying to/from pods.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cp/>.

- Copy a local file to a pod:

`kubectl cp {{path/to/local_file}} {{pod_name}}:/{{path/in/pod}}`

- Copy a file from a pod to the local machine:

`kubectl cp {{pod_name}}:{{/path/in/pod/file}} {{path/to/local_destination}}`

- Copy a directory recursively from the local machine to a pod:

`kubectl cp {{path/to/local_directory}} {{pod_name}}:{{/path/in/pod}}`

- Copy from/to a pod in a specific namespace:

`kubectl cp {{namespace}}/{{pod_name}}:{{/path/in/pod}} {{path/to/local_destination}}`

- Use a specific container in a multi-container pod:

`kubectl cp {{pod_name}}:{{/path/in/pod}} {{path/to/local_destination}} -c {{container_name}}`
