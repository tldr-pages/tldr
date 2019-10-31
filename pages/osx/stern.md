# Stern

> Tail Logs from multiple pods and multiple containers on Kubernetes.
> More information: <https://github.com/wercker/stern>.

- Tail logs from specific namespace:

`stern <POD> --container <CONTAINER> --namespace <NAMESPACE>`

- Tail logs using particular kubeconfig:

`stern <POD> --container <CONTAINER> --kubeconfig <KUBECONFIG_PATH>`

- Tail logs since last 2 hours:

`stern <POD> --container <CONTAINER> --since 2h`

- Tail logs from pods having label "KEY1=VALUE1,KEY2=VALUE2" across all namespaces:

`stern --container <CONTAINER> -l "KEY1=VALUE1,KEY2=VALUE2" --all-namespaces`

- Tail logs from containers whose name starts with "XYZ":

`stern <POD> --container "XYZ*"`
