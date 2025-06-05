# devspace

> DevSpace is a tool that accelerates developing, deploying and debugging applications with Docker and Kubernetes.
> More information: <https://devspace.sh>.

- Initialize a new DevSpace project within the current directory:

`devspace init`

- Initialize a project using a specific Dockerfile:

`devspace init --dockerfile {{path/to/Dockerfile}}`

- Start development mode with port forwarding, file synchronization and terminal:

`devspace dev`

- Start development mode with a specific namespace:

`devspace dev -n {{namespace}}`

- Deploy the project to Kubernetes:

`devspace deploy`

- Deploy the project with a specific profile:

`devspace deploy -p {{profile-name}}`

- Build all defined images and push them:

`devspace build`

- Build and tag images with a specific tag:

`devspace build -t {{tag}}`

- Display the logs of a pod:

`devspace logs`

- Display the logs of a specific container within a pod:

`devspace logs -c {{container}}`

- Follow the logs of a pod:

`devspace logs -f`

- Open a shell to a container:

`devspace enter`

- Open a shell to a specific container:

`devspace enter -c {{container}}`

- Synchronize local files to a container:

`devspace sync --path {{./local-path}}:{{/remote-path}}`

- Synchronize with specific exclude patterns:

`devspace sync --path {{./local-path}}:{{/remote-path}} --exclude={{node_modules,test}}`

- Analyze a Kubernetes namespace for potential problems:

`devspace analyze`

- Analyze with patience, waiting for resources to become ready:

`devspace analyze --patient`

- Render the Kubernetes manifests that would be deployed:

`devspace render`

- Purge all deployed resources:

`devspace purge`

- Purge with force, even if resources might be in use by another project:

`devspace purge --force-purge`

- Open the DevSpace UI in the browser:

`devspace ui`

- Open the DevSpace UI with a specific port:

`devspace ui --port {{port}}`

- Attach to a running container:

`devspace attach`

- Attach to a specific container:

`devspace attach -c {{container}}`

- Display the version information:

`devspace version`
