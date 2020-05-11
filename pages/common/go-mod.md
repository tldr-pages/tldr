# go mod

> Module maintenance.
> More information: <https://golang.org/cmd/go/#hdr-Module_maintenance>.

- Initialize new module in current directory:

`go mod init {{moduleName}}`

- Download modules to local cache:

`go mod download`

- Add missing and remove unused modules:

`go mod tidy`

- Verify dependencies have expected content:

`go mod verify`

- Copy all dependencies sources into vendor directory:

`go mod vendor`
