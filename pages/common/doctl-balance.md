# doctl balance

> Show the balance of a Digital Ocean account.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/balance/>.

- Get balance of the account associated with the current context:

`doctl balance {{[g|get]}}`

- Get the balance of an account associated with an access token:

`doctl balance {{[g|get]}} {{[-t|--access-token]}} {{access_token}}`

- Get the balance of an account associated with a specified context:

`doctl balance {{[g|get]}} --context`
