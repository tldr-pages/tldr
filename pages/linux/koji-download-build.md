# koji download-build

> Download a built package.
> More information: <https://docs.pagure.org/koji>.

- Download all RPMs from a specific build:

`koji download-build {{BuildID|RPM|NVR}}`

- Download RPMs signed with the given key:

`koji download-build --key {{key}} {{BuildID|RPM|NVR}}`

- Only download RPMs for given arch:

`koji download-build --arch {{x86_64,aarch64,noarch,...}} {{BuildID|RPM|NVR}}`

- Download the given RPM:

`koji download-build --rpm {{RPM}}`

- Display help:

`koji download-build --help`
