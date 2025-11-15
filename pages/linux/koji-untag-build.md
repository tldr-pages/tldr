# koji untag-build

> Remove a tag from one or more builds.
> More information: <https://docs.pagure.org/koji>.

- Remove a tag from one or more builds:

`koji untag-build {{tag}} {{NVR1 NVR2 ...}}`

- Untag all versions of the package in this tag:

`koji untag-build {{tag}} {{pkg1 pkg2 ...}} --all`

- Untag all versions of the package in this tag except the latest:

`koji untag-build {{tag}} {{pkg1 pkg2 ...}} --non-latest`

- Test mode:

`koji untag-build {{tag}} {{NVR1 NVR2 ...}} {{[-n|--test]}}`

- Print details:

`koji untag-build {{tag}} {{NVR1 NVR2 ...}} {{[-v|--verbose]}}`

- Display help:

`koji untag-build --help`
