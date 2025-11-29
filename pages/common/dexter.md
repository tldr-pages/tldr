# dexter

> Authenticate the `kubectl` users with OpenId Connect.
> More information: <https://github.com/gini/dexter#run-dexter>.

- Create and authenticate a user with Google OIDC:

`dexter auth {{[-i|--client-id]}} {{client_id}} {{[-s|--client-secret]}} {{client_secret}}`

- Override the default kube configuration file location:

`dexter auth {{[-i|--client-id]}} {{client_id}} {{[-s|--client-secret]}} {{client_secret}} {{[-k|--kube-config]}} {{sample/config}}`
