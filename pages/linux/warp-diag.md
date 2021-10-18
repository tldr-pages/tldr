# warp-diag

> Diagnostic and feedback tool for Cloudflare's WARP service (`warp-cli`).
> More information: <https://developers.cloudflare.com/warp-client/setting-up/linux>.

- Generate a complete zipped log file of the `warp-cli` process:

`warp-diag`

- Set if timestamp should be added to output file name:

`warp-diag --add-ts`

- Save the output file under a specific directory:

`warp-diag --output {{path/to/directory}}`

- Submit a new feedback to Cloudflare's WARP interactively:

`warp-diag feedback`
