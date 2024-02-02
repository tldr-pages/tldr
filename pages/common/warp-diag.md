# warp-diag

> Diagnostic and feedback tool for Cloudflare's WARP service.
> See also: `warp-cli`.
> More information: <https://developers.cloudflare.com/warp-client/>.

- Generate a `zip` file with information about the system configuration and the WARP connection:

`warp-diag`

- Generate a `zip` file with debug information including a timestamp to the output filename:

`warp-diag --add-ts`

- Save the output file under a specific directory:

`warp-diag --output {{path/to/directory}}`

- Submit a new feedback to Cloudflare's WARP interactively:

`warp-diag feedback`
