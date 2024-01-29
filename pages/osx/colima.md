# colima

> Container runtimes on macOS (and Linux) with minimal setup.
> More information: <https://github.com/abiosoft/colima>.

- Start Colima:
  
`colima start`

- Use a config file:

`colima start --edit`

- Starts and setup Containerd. You can use colima nerdctl to interact with Containerd using nerdctl. It is recommended to run colima nerdctl install to install nerdctl alias script in $PATH:

`colima start --runtime containerd`

- Start with Kubernetes. `kubectl` is required. `brew install kubectl`:

`colima start --kubernetes`

- Customize runtime:
  
`colima start --cpu 4 --memory 8 --disk 100`
  
- Start Colima and use Docker:

`brew install docker && colima start && docker run hello-world`

- Show status of various containers:

`colima list`

- Rrun time status:

`colima status`
