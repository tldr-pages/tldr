# helm list

> List helm releases.
> More information: <https://helm.sh/docs/helm/helm_list/>.

- List releases in the current namespace:

`helm list`

- List releases in all namespaces:

`helm list {{[-A|--all-namespaces]}}`

- List releases in a specific namespace:

`helm list {{[-n|--namespace]}} {{namespace}}`

- List releases whose names match a `regex`:

`helm list {{[-f|--filter]}} {{regex}}`

- List releases with a specific status:

`helm list --{{deployed|failed|pending|uninstalled}}`

- List only the names of the releases:

`helm list {{[-q|--short]}}`

- List releases in JSON or YAML format:

`helm list {{[-o|--output]}} {{json|yaml}}`

- List releases sorted by date:

`helm list {{[-d|--date]}}`
