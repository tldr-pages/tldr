# colima

> Container runtimes for macOS and Linux with minimal setup.
> More information: <https://github.com/abiosoft/colima>.

- Start Colima:

`colima start`

- Use a config file:

`colima start --edit`
  
- Start and setup Containerd. Install nerdctl to use Containerd via nerdctl:

`colima start --runtime containerd`

- Start with Kubernetes. `kubectl` is required:  

`colima start --kubernetes`

- Customize CPU, memory, disk:

`colima start --cpu {{4}} --memory {{8}} --disk {{100}}`
  
- Use Docker via Colima:

`brew install docker && colima start && docker run hello-world`

- Show container status:

`colima list`
  
- Show runtime status:

`colima status`
