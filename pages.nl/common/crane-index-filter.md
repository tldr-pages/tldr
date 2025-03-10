# crane index filter

> Wijzigt een remote index door te filteren op basis van platform.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_filter.md>.

- Wijzig de remote index:

`crane index filter`

- Specificeer het platform(en) dat je wilt behouden uit de basis in de vorm os/arch{{/variant}}{{:osversion}}{{,<platform>}}:

`crane index filter --platform {{platform1 platform2 ...}}`

- Tag die toegepast moet worden op de resulterende image:

`crane index filter {{[-t|--tags]}} {{tag_naam}}`

- Toon de help:

`crane index filter {{[-h|--help]}}`
