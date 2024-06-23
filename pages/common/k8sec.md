# k8sec

> Manage Kubernetes secrets.
> More information: <https://github.com/dtan4/k8sec>.

- List all secrets:

`k8sec list`

- List a specific secret as a base64-encoded string:

`k8sec list {{secret_name}} --base64`

- Set a secret's value:

`k8sec set {{secret_name}} {{key=value}}`

- Set a base64-encoded value:

`k8sec set --base64 {{secret_name}} {{key=encoded_value}}`

- Unset a secret:

`k8sec unset {{secret_name}}`

- Load secrets from a file:

`k8sec load -f {{path/to/file}} {{secret_name}}`

- Dump secrets to a file:

`k8sec dump -f {{path/to/file}} {{secret_name}}`
