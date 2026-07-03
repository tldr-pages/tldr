# cloudflared access curl

> Send a curl request to a Cloudflare Access protected URL, injecting the Access token.
> See also: `cloudflared access login`, `cloudflared access token`.
> More information: <https://developers.cloudflare.com/cloudflare-one/>.

- Send a request to a protected application:

`cloudflared access curl {{https://app.example.com}}`

- Pass additional arguments through to `curl`:

`cloudflared access curl {{https://app.example.com}} {{-X POST -d @data.json}}`

- Send the request without requiring a cached token:

`cloudflared access curl {{[-ar|--allow-request]}} {{https://app.example.com}}`