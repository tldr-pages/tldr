# crane mutate

> Modify image labels and annotations.
> The container must be pushed to a registry, and the manifest is updated there.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_mutate.md>.

- Set new annotations or labels:

`crane mutate {{[-a|--annotation]}}/{{[-l|--label]}} {{annotation/label}}`

- Append a tarball, or set the command/entrypoint/environment variables/exposed ports of an image:

`crane mutate {{--append}}/{{--cmd}}/{{--entrypoint}}/{{[-e|--env]}}/{{--exposed-ports}} {{var1 var2 ...}}`

- Write the resulting image to a new tarball:

`crane mutate {{[-o|--output]}} {{path/to/tarball}}`

- Set the platform of the mutated image in the form `os/arch/variant:osversion,platform`:

`crane mutate --set-platform {{platform_name}}`

- Apply a new tag reference to the mutated image:

`crane mutate {{[-t|--tag]}} {{tag_name}}`

- Set a new user:

`crane mutate {{[-u|--user]}} {{username}}`

- Set a new working directory:

`crane mutate {{[-w|--workdir]}} {{path/to/work_directory}}`

- Display help:

`crane mutate {{[-h|--help]}}`
