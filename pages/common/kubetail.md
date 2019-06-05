# kubetail

> Utility to tail multiple Kubernetes pod logs at the same time.
> More information: <https://github.com/johanhaleby/kubetail>.

- Tail the logs of multiple pods (whose name starts with "my_app") in one go:

`kubetail {{my_app}}`

- Tail only a specific container from multiple pods:

`kubetail {{my_app}} -c {{my_container}}`

- To tail multiple containers from multiple pods:

`kubetail {{my_app}} -c {{my_container_1}} -c {{my_container_2}}`

- To tail multiple applications at the same time separate them by comma:

`kubetail {{my_app_1}},{{my_app_2}}`
