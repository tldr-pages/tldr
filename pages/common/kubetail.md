# kubetail

> Utility to tail multiple Kubernetes pod logs at the same time.
> More information: <https://github.com/johanhaleby/kubetail>.

- Tail the logs of multiple pods (whose name starts with `app_name`) in one go:

`kubetail {{app_name}}`

- Tail only a specific container from multiple pods:

`kubetail {{app_name}} {{[-c|--container]}} {{container_name}}`

- Tail multiple containers from multiple pods:

`kubetail {{app_name}} {{[-c|--container]}} {{container_name_1}} {{[-c|--container]}} {{container_name_2}}`

- Tail multiple applications at the same time separate them by comma:

`kubetail {{app_name_1,app_name_2,...}}`
