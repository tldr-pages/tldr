# devspace

> Develop, deploy, and debug applications inside Kubernetes.
> More information: <https://devspace.sh/docs/cli>.

- Initialize a new DevSpace project in the current directory:

`devspace init`

- Start development mode with port forwarding, file synchronization, and terminal access:

`devspace dev`

- Start development mode in a specific namespace:

`devspace dev {{[-n|--namespace]}} {{namespace}}`

- Deploy the project to Kubernetes:

`devspace deploy`

- Deploy the project with a specific profile:

`devspace deploy {{[-p|--profile]}} {{profile-name}}`

- Build all defined images:

`devspace build`

- Follow logs from a pod:

`devspace logs {{[-f|--follow]}}`

- Open the DevSpace UI in the browser:

`devspace ui`
