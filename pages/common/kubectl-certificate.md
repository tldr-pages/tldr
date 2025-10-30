# kubectl certificate

> Manage certificate signing requests.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_certificate>.

- Approve a certificate signing request by name:

`kubectl certificate approve {{csr_name}}`

- Deny a certificate signing request by name:

`kubectl certificate deny {{csr_name}}`

- Approve a certificate signing request defined in a manifest file:

`kubectl certificate approve --filename {{path/to/csr.yaml}}`

- Deny a certificate signing request defined in a manifest file:

`kubectl certificate deny --filename {{path/to/csr.yaml}}`

- Force reapproval of a certificate signing request that was previously denied:

`kubectl certificate approve --force {{csr_name}}`

