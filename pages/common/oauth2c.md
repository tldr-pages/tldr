# oauth2c

> Interact with OAuth 2.0 authorization servers.
> More information: <https://github.com/cloudentity/oauth2c>.

- Fetch an access token using client credentials:

`oauth2c {{issuer_url}} --client-id {{client_id}} --client-secret {{client_secret}}`

- Fetch a token using authorization code flow:

`oauth2c {{issuer_url}} --client-id {{client_id}} --response-types code`

- Fetch a token using authorization code with PKCE:

`oauth2c {{issuer_url}} --client-id {{client_id}} --pkce`

- Fetch a token using password credentials:

`oauth2c {{issuer_url}} --client-id {{client_id}} --username {{username}} --password {{password}}`

- Refresh an existing access token:

`oauth2c {{issuer_url}} --client-id {{client_id}} --refresh-token {{refresh_token}}`

- Fetch a token with specific scopes:

`oauth2c {{issuer_url}} --client-id {{client_id}} --scopes {{scope1,scope2}}`

- Use device authorization flow:

`oauth2c {{issuer_url}} --client-id {{client_id}} --grant-type device_code`

- Run in silent mode without browser:

`oauth2c {{issuer_url}} --client-id {{client_id}} --silent --no-browser`
