# devspace

> DevSpace accelerates developing, deploying, and debugging applications with Docker and Kubernetes.
> More information: <https://devspace.sh>.

- Initialize a new DevSpace project in the current directory:
  `devspace init`

- Start development mode with port forwarding, file sync, and terminal access:
  `devspace dev`

- Start development mode with a specific namespace:
  `devspace dev -n {{namespace}}`

- Deploy the project to Kubernetes:
  `devspace deploy`

- Deploy the project with a specific profile:
  `devspace deploy -p {{profile-name}}`

- Build all defined images:
  `devspace build`

- Follow logs from a pod:
  `devspace logs -f`

- Open the DevSpace UI in the browser:
  `devspace ui`
