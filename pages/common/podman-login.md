# podman login

> Log in to a container registry.
> Note: The default authfile path on Linux is `$XDG_RUNTIME_DIR/containers/auth.json`, which is usually stored in a `tmpfs` (in RAM).
> More information: <https://docs.podman.io/en/latest/markdown/podman-login.1.html>.

- Log in to a registry (non-persistent on Linux; persistent on Windows/macOS):

`podman login {{registry.example.org}}`

- Log in to a registry persistently on Linux:

`podman login --authfile $HOME/.config/containers/auth.json {{registry.example.org}}`

- Log in to an insecure (HTTP) registry:

`podman login --tls-verify false {{registry.example.org}}`
