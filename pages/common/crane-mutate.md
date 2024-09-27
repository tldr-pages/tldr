# crane mutate

> Modify image labels and annotations.
> The container must be pushed to a registry, and the manifest is updated there.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_mutate.md>.

- New annotations to set (default []):

`crane mutate {{-a|--annotaiton}}/{{-l|--label}} {{strinToString}}`

- Path to tarball/command/entrypoint/environment variable/exposed-ports to append to image:

`crane mutate {{--append}}/{{--cmd}}/{{--entrypoint}}/{{-e|--env}}/{{--exposed-ports}} {{strings}}`

- Display help:

`crane mutate {{-h|--help}}`

- Path to new tarball of resulting image:

`crane mutate {{-o|--output}} {{string}}`

- Repository to push mutated image:

`crane mutate {{--set-platform}} {{string}}`

- New tag reference to apply to mutated image:

`crane mutate {{-t|--tag}} {{string}}`

- New user to set:

`crane mutate {{-u|--user}} {{string}}`

- New working dir to set:

`crane mutate {{-w|--workdir}} {{string}}`
