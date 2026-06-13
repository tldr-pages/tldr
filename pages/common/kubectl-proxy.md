# kubectl proxy

> Create a proxy server or application-level gateway between localhost and the Kubernetes API server.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_proxy/>.

- Run a proxy using the default settings on port 8001 and listen on localhost:

`kubectl proxy`

- Proxy part of the Kubernetes API while serving static files from a local directory:

`kubectl proxy {{[-w|--www]}} {{path/to/static_dir}} {{[-P|--www-prefix]}} {{/static_prefix/}} --api-prefix {{/api_subset/}}`

- Proxy the entire Kubernetes API under a custom prefix:

`kubectl proxy --api-prefix {{/custom_prefix/}}`

- Serve the Kubernetes API on a specific port while also serving static content:

`kubectl proxy {{[-p|--port]}} {{port}} {{[-w|--www]}} {{path/to/static_dir}}`

- Run a proxy on a random local port, printing the chosen port to `stdout`:

`kubectl proxy {{[-p|--port]}} 0`

- Run the proxy on a Unix domain socket instead of a TCP port:

`kubectl proxy {{[-u|--unix-socket]}} {{path/to/socket}}`

- Accept connections from remote hosts by listening on all interfaces (use caution when exposing the proxy publicly):

`kubectl proxy --address 0.0.0.0 --accept-hosts '.*'`

- Allow only selected API paths while rejecting sensitive endpoints:

`kubectl proxy --accept-paths '^/api/v1/namespaces/default/.*' --reject-paths '^/api/.*/pods/.*/exec'`
