# crane index filter

> Modifies a remote index by filtering based on platform.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_filter.md>.

- Modify remote index:

`crane index filter`

- Specify the platform(s) to keep from base in the form os/arch{{/variant}}{{:osversion}}{{,<platform>}}:

`crane index filter --platform {{platform1 platform2 ...}}`

- Tag to apply to resulting image:

`crane index filter {{[-t|--tags]}} {{tag_name}}`

- Display help:

`crane index filter {{[-h|--help]}}`
