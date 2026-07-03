# cloudflared tunnel diag

> Create a diagnostic report from a local cloudflared instance.
> More information: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>.

- Create a diagnostic report for the local instance:

`cloudflared tunnel diag`

- Target a specific instance by its metrics address:

`cloudflared tunnel --metrics {{localhost:port}} diag`

- Collect logs from a specific container:

`cloudflared tunnel diag --diag-container-id {{container_id}}`

- Create the report without collecting logs:

`cloudflared tunnel diag --no-diag-logs`