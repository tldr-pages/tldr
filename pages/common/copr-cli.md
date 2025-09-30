# copr-cli

> Interface with Fedora-Projects copr instance for building RPMs and publishing them.
> More information: <https://manned.org/copr-cli>.

- Show user logged in to copr:

`copr-cli whoami`

- Build a local spec file on copr:

`copr-cli build {{repository}} {{path/to/spec_file}}`

- Check status of builds:

`copr-cli list-builds {{repository}}`

- Trigger a copr build of a spec-file from public (Git) repository:

`copr-cli buildscm {{repository}} --clone-url {{https://git.example.org/repo}} --spec {{spec_file_name}}`
