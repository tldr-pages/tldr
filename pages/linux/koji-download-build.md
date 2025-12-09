# koji download-build

> Download a built package.
> More information: <https://docs.pagure.org/koji>.

- Download all RPMs from a specific build:

`koji download-build {{BuildID|RPM|NVR}}`

- Download RPMs signed with the given key:

`koji download-build {{BuildID|RPM|NVR}} --key {{key}}`

- Only download RPMs for given arch:

`koji download-build {{BuildID|RPM|NVR}} --arch {{x86_64,aarch64,noarch,...}}`

- Download the given RPM:

`koji download-build {{RPM}} --rpm`

- Display help:

`koji download-build {{[-h|--help]}}`
