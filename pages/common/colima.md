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

- Customize CPU numbers, memory and disk space (in GiB):

`colima start --cpu {{number}} --memory {{storage_space}} --disk {{storage_space}}`

- Use Docker via Colima (Note: this requires Docker to be preinstalled):

`colima start`

- List containers, showing their information and status:

`colima list`

- Show runtime status:

`colima status`
