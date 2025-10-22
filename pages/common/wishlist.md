# wishlist

> SSH directory and multiplexer from Charmbracelet.
> Acts as a single entry point for connecting to SSH servers or Wish applications.
> More information: <https://github.com/charmbracelet/wishlist>.

- Explore SSH servers listed in your `~/.ssh/config` file (local mode):

`wishlist`

- Start Wishlist in server mode to provide remote access:

`wishlist {{[s|serve]}}`

- Use a custom configuration file:

`wishlist {{[-c|--config]}} {{path/to/config.yaml}}`

- Discover SSH endpoints using Zeroconf (mDNS/Bonjour):

`wishlist --zeroconf.enabled`

- Discover SSH nodes from DNS SRV records:

`wishlist --srv.domain {{example.com}}`

- Discover SSH nodes from a Tailscale tailnet:

`wishlist --tailscale.net={{tailnet_name}} --tailscale.key={{tskey-api-abc123}}`

- Run Wishlist in Docker:

`docker run -p 2222:22 -v $PWD/.wishlist:/wishlist docker.io/charmcli/wishlist:latest`
