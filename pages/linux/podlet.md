# podlet

> Generate Podman Quadlet files from a Podman command, compose file, or existing object.
> See also: `podman`.
> More information: <https://github.com/containers/podlet>.

- Generate the equivalent Quadlet for a podman command:

`podlet {{podman_command}}`

- Set an explicit name and description for the generated Quadlet:

`podlet {{[-n|--name]}} {{name}} {{[-d|--description]}} {{description}} {{podman_command}}`

- Add startup dependency and ordering declarations to the generated Quadlet:

`podlet {{[-i|--install]}} --wanted-by {{unit}} --after {{unit}} {{podman_command}}`

- Generate Quadlets for a compose file in the current directory with a well-known name (`(docker-)?compose\.ya?ml`):

`podlet compose`

- Generate Quadlets for a compose file into the unit directory of the current user:

`podlet {{[-u|--unit-directory]}} compose {{path/to/compose.yaml}}`
