# crane index append

> Append manifest to a remote index.
> This sub-command pushes an index based on an (optional) base index, with appended manifests.
> The platform for appended manifests is inferred from the configuration file or omitted if that is infeasible.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_append.md>.

- Append manifest to a remote index:

`crane index append`

- Append specific manifests to the base index:

`crane index append {{[-m|--manifest]}} {{manifest_name1 manifest_name2 ...}}`

- Apply a tag to the resulting image:

`crane index append {{[-t|--tag]}} {{tag_name}}`

- Use Docker media types instead of OCI for an empty base index:

`crane index append --docker-empty-base`

- Append each of its children rather than the index itself (defaults true):

`crane index append --flatten`

- Display help:

`crane index append {{[-h|--help]}}`
