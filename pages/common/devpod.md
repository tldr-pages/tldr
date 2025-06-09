# devpod

> Launch reproducible development environments using Docker, Kubernetes, or SSH.
> More information: <https://devpod.sh/docs/quickstart/devpod-cli/>.

- Install the DevPod CLI on Linux:

`curl {{[-L|--location]}} {{[-o|--output]}} devpod https://github.com/loft-sh/devpod/releases/latest/download/devpod-linux-amd64 && sudo install -m0755 devpod /usr/local/bin`

- Add a provider such as Docker or Kubernetes:

`devpod provider add {{provider_name}}`

- List all available providers:

`devpod provider list-available`

- Start a workspace from a GitHub repository with a specific IDE:

`devpod up {{github.com/user/repo}} {{[-i|--ide]}} {{vscode}}`

- Start a workspace from a local directory:

`devpod up {{path/to/project}}`

- Recreate an existing workspace:

`devpod up {{workspace_name}} {{[-r|--recreate]}}`

- Reset a workspace to a clean state:

`devpod up {{workspace_name}} {{[-x|--reset]}}`

- Add a custom provider from a GitHub repository:

`devpod provider add {{org/provider-repo}}`
