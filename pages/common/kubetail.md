# kubetail

> Utility to tail multiple Kubernetes pod logs at the same time.
> More information: <https://github.com/johanhaleby/kubetail>.

- Tail the logs of multiple pods (whose name starts with "my_app") in one go:

`kubetail {{my_app}}`

- Tail only a specific container from multiple pods:

`kubetail {{my_app}} {{[-c|--container]}} {{my_container}}`

- Tail multiple containers from multiple pods:

`kubetail {{my_app}} {{[-c|--container]}} {{my_container1}} {{[-c|--container]}} {{my_container2}}`

- Tail multiple applications at the same time separate them by comma:

`kubetail {{my_app1,my_app2,...}}`
