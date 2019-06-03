# dexter

> Tool for authenticating the kubectl users with OpenId Connect.
> More information: <https://github.com/gini/dexter>.

- Create and authenticate a user with Google OIDC:

`dexter auth -i {{client-id}} -s {{client-secret}}`

- Override the default kube config location:

`dexter auth -i {{client-id}} -s {{client-secret}} --kube-config {{sample/config}}`
