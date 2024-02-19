# dexter

> Authenticate the `kubectl` users with OpenId Connect.
> More information: <https://github.com/gini/dexter>.

- Create and authenticate a user with Google OIDC:

`dexter auth -i {{client_id}} -s {{client_secret}}`

- Override the default kube configuration file location:

`dexter auth -i {{client_id}} -s {{client_secret}} --kube-config {{sample/config}}`
