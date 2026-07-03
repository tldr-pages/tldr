# cloudflared tunnel ready

> Query the local cloudflared `/ready` endpoint and return an exit code based on tunnel readiness.
> More information: <https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/configure-tunnels/cloudflared-parameters/>.

- Check whether the local tunnel has at least one ready connection:

`cloudflared tunnel ready`

- Check readiness for an instance exposing metrics on a specific address:

`cloudflared tunnel --metrics {{localhost:port}} ready`