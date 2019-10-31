# Stern

> Tail Logs form multiple pods and multiple containers on Kubernetes.
> Reference: <https://github.com/wercker/stern>.

- Tail logs of container "nginx" inside pod "nginx-pod" from namespace "production":

`stern nginx-pod --container nginx --namespace "production"`

- Tail logs of container "nginx" inside pod "nginx-pod" using particular kubeconfig:

`stern nginx-pod --container nginx --kubeconfig "~/.kube/config_prod"`

- Tail logs since last 2 hours from container "nginx" inside pod "nginx-pod" from namespace "production":

`stern nginx-pod --container nginx --namespace "production" --since 2h`

- Tail logs of container "nginx" inside pods with label "component=serving,app=nginx" across all namespaces :

`stern --container nginx -l "component=serving,app=nginx" --all-namespaces`

