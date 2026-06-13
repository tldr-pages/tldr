# nerdctl

> Docker-compatible CLI for containerd.
> More information: <https://github.com/containerd/nerdctl/blob/main/docs/command-reference.md>.

- List all containers (running and stopped):

`nerdctl ps {{[-a|--all]}}`

- Start a container from an image, with a custom name:

`nerdctl run --name {{container_name}} {{image}}`

- Start or stop an existing container:

`nerdctl {{start|stop}} {{container_name}}`

- Pull an image from a container registry:

`nerdctl pull {{image}}`

- Display the list of already downloaded images:

`nerdctl images`

- Open an interactive tty with Bourne shell (`sh`) inside a running container:

`nerdctl exec {{[-it|--interactive --tty]}} {{container_name}} sh`

- Remove stopped containers:

`nerdctl rm {{container1 container2 ...}}`

- Fetch and follow the logs of a container:

`nerdctl logs {{[-f|--follow]}} {{container_name}}`
