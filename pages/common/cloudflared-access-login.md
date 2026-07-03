# cloudflared access login

> Authenticate with an identity provider for a Cloudflare Access protected application and cache the token locally.
> See also: `cloudflared access token`, `cloudflared access curl`.
> More information: <https://developers.cloudflare.com/cloudflare-one/identity/authorization-cookie/>.

- Authenticate to a Cloudflare Access protected application:

`cloudflared access login {{https://app.example.com}}`

- Authenticate without printing the token to the command line:

`cloudflared access login {{[-q|--quiet]}} {{https://app.example.com}}`

- Authenticate and print only the token to `stdout`:

`cloudflared access login --no-verbose {{https://app.example.com}}`

- Automatically close the browser authentication page after logging in:

`cloudflared access login --auto-close {{https://app.example.com}}`