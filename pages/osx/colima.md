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

- Customize CPU, memory, disk:

`colima start --cpu {{4}} --memory {{8}} --disk {{100}}`

- Use Docker via Colima:

`brew install docker && colima start`

- List containers, showing their information and status:

`colima list`

- Show runtime status:

`colima status`
