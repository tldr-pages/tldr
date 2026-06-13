# trip

> A network diagnostic tool.
> Combines the functionality of `traceroute` and `ping`.
> Designed to assist with the analysis of networking issues.
> More information: <https://trippy.rs/reference/cli/>.

- Basic usage with default parameters:

`sudo trip {{example.com}}`

- Trace without requiring elevated privileges (supported platforms only):

`trip {{example.com}} --unprivileged`

- Trace using `IPv6` only:

`sudo trip {{example.com}} --ipv6`

- Trace using the `udp` protocol:

`sudo trip {{example.com}} --protocol {{udp}}`

- Use custom destination port `443` for `tcp` tracing:

`sudo trip {{example.com}} --protocol {{tcp}} --target-port {{443}}`

- Use custom source port `5000` for `udp` tracing:

`sudo trip {{example.com}} --protocol {{udp}} --source-port {{5000}}`
