# podman login

> Log in bij een containerregister.
> Opmerking: het standaard authfile-pad op Linux is `$XDG_RUNTIME_DIR/containers/auth.json`, dat meestal is opgeslagen in een `tmpfs` (in RAM).
> Meer informatie: <https://docs.podman.io/en/latest/markdown/podman-login.1.html>.

- Log in bij een register (niet-persistent op Linux; persistent op Windows/macOS):

`podman login {{registry.example.org}}`

- Log persistent in bij een register op Linux:

`podman login --authfile $HOME/.config/containers/auth.json {{registry.example.org}}`

- Log in bij een onveilig (HTTP-)register:

`podman login --tls-verify false {{registry.example.org}}`
