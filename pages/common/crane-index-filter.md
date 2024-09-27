# crane index filter

> Modifies a remote index by filtering based on platform.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_filter.md>.

- Modify remote index:

`crane index filter`

- Display help:

`crane index filter {{-h|--help}}`

- Specify the platform(s) to keep from base in the form os/arch{{/variant}}{{:osversion}}{{,<platform>}}:

`crane index filter {{--platform}} {{platform(s)}}`

- Tag to apply to resulting image:

`crane index filter {{-t|--tags}} {{string}}`
