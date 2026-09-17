# ots

> Share end-to-end encrypted secrets using a one-time-viewable URL.
> More information: <https://github.com/sniptt-official/ots>.

- Create new secret:

`ots new`

- Create new secret and specify hours until expiry (default is 24):

`ots new -x {{number_of_hours}}h`

- Specify region of server to store secret (default is `us-east-1`):

`ots new --region {{regional_server_id}}`
