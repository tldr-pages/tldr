# spatial

> A set of commands for managing and developing SpatialOS projects.

- Build workers for local deployment on Unity on Windows:

`spatial worker build --target=development --target=Osx`

- Build workers for local deployment on Unreal:

`spatial worker build --target=local --target=Windows`

- Deploy locally:

`spatial local launch {{launch_config}} --snapshot={{snapshot_file}}`

- Launch a local worker to connect to your local deployment:

`spatial local worker launch UnityClient default`

- Upload an assembly to use for cloud deployments:

`spatial cloud upload {{assembly_name}}>`

- Launch a cloud deployment:

`spatial cloud launch {{assembly_name}} {{launch_config}} {{deployment_name}}`
