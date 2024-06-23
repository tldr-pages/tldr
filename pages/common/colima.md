# colima

> Container runtimes for macOS and Linux with minimal setup.
> More information: <https://github.com/abiosoft/colima>.

- Start the daemon in the background:

`colima start`

- Create a configuration file and use it:

`colima start --edit`

- Start and setup containerd (install `nerdctl` to use containerd via `nerdctl`):

`colima start --runtime containerd`

- Start with Kubernetes (`kubectl` is required):

`colima start --kubernetes`

- Customize CPU count, RAM memory and disk space (in GiB):

`colima start --cpu {{number}} --memory {{memory}} --disk {{storage_space}}`

- Use Docker via Colima (Docker is required):

`colima start`

- List containers with their information and status:

`colima list`

- Show runtime status:

`colima status`
