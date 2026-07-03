# cloudflared access token

> Fetch a JSON Web Token (JWT) to authenticate requests to a Cloudflare Access protected application.
> See also: `cloudflared access login`, `cloudflared access curl`.
> More information: <https://developers.cloudflare.com/cloudflare-one/>.

- Print the token for a protected application:

`cloudflared access token --app={{https://app.example.com}}`