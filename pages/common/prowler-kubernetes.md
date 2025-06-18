# prowler kubernetes

> Assess Kubernetes cluster security best practices and configurations.
> See also: `prowler`, `prowler-aws`, `prowler-azure`, `prowler-gcp`, `prowler-m365`, `prowler-github`.
> More information: <https://docs.prowler.com/projects/prowler-open-source/en/latest/>.

- Run the default checks using the default kubeconfig location:

`prowler kubernetes`

- Specify a custom kubeconfig file for scanning:

`prowler kubernetes --kubeconfig-file {{path/to/kubeconfig}}`

- Specify a specific Kubernetes context to scan:

`prowler kubernetes --context {{my-context}}`

- Scan specific namespaces only:

`prowler kubernetes --namespaces {{default}} {{kube-system}}`

- Run checks for selected Kubernetes services:

`prowler kubernetes {{[-s|--services]}} {{ietcd apiserver ...}}`

- Run a specific Kubernetes check:

`prowler kubernetes {{[-c|--checks]}} {{etcd_encryption}}`

- Exclude specific checks or services:

`prowler kubernetes {{[-e|--excluded-checks]}} {{etcd_encryption}} --exclude-services {{ietcd apiserver ...}}`
