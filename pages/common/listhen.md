# listhen

> Elegant HTTP listener with automatic port detection, HTTPS self-signed certificates, and tunnel support.
> More information: <https://github.com/unjs/listhen>.

- Start a local server for an exported request handler file:

`listhen {{./server.ts}}`

- Listen on a specific port and bind to all network interfaces:

`listhen {{./server.ts}} --port {{3000}} --host`

- Open the server URL in the default browser and enable file watching:

`listhen {{./server.ts}} --open --watch`

- Expose the local server publicly via a tunnel:

`listhen {{./server.ts}} --tunnel`
