# Stern

> Tail Logs from multiple pods and multiple containers on Kubernetes.
> More information: <https://github.com/wercker/stern>.

- Tail logs from a specific namespace:

`stern {{pod_name}} --container {{container}} --namespace {{namespace}}`

- Tail logs using a particular configuration file:

`stern {{pod_name}} --container {{container}} --kubeconfig {{path/to/kubeconfig_file}}`

- Display the last 2 hours worth of logs, tailing for newer ones:

`stern {{pod_name}} --container {{container}} --since {{2h}}`

- Tail logs from pods that have specific labels across all namespaces:

`stern --container {{container}} -l "{{KEY1=VALUE1,KEY2=VALUE2}}" --all-namespaces`

- Tail logs from containers whose name starts with "XYZ":

`stern {{pod_name}} --container "{{XYZ*}}"`
