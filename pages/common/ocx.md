# ocx

> Manage opencodex, a local proxy that connects Codex to other model providers.
> More information: <https://opencodex.me/reference/cli/>.

- Set up providers and configure Codex interactively:

`ocx setup`

- Start the proxy and sync available models to Codex:

`ocx start`

- Start the proxy on a specific port:

`ocx start --port {{8080}}`

- Check whether the proxy is running:

`ocx status`

- Refresh provider models in the Codex configuration:

`ocx sync`

- Open the web dashboard:

`ocx gui`

- Stop the proxy and restore the native Codex configuration:

`ocx stop`
