# doppler secrets

> Manage your Doppler project's secrets.
> More information: <https://docs.doppler.com/docs/accessing-secrets>.

- Get all secrets:

`doppler secrets`

- Get value(s) of one or more secrets:

`doppler secrets get {{secrets}}`

- Upload a secrets file:

`doppler secrets upload {{path/to/file.env}}`

- Delete value(s) of one or more secrets:

`doppler secrets delete {{secrets}}`

- Download secrets as `.env`:

`doppler secrets download --format=env --no-file > {{path/to/.env}}`
