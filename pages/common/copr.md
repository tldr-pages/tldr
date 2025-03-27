# copr

> Interface with Fedora-Projects copr instance for building RPMs and publishing them.
> More information: <https://developer.fedoraproject.org/deployment/copr/copr-cli.html>.

- Show user logged in to copr:

`copr whoami`

- Build a local spec file on copr:

`copr build {{repository}} {{path/to/spec_file}}`

- Check status of builds:

`copr list-builds {{repository}}`

- Trigger a copr build of a spec-file from public (git) repository:

`copr buildscm {{repository}} --clone-url {{https://git.example.org/repo}} --spec {{spec_file_name}}`
