# spatial

> A set of commands for managing and developing SpatialOS projects.

- Run this when you use a project for the first time:

`spatial worker build`

- Build workers for local deployment on Unity on macOS:

`spatial worker build --target=development --target=Osx`

- Build workers for local deployment on Unreal on Windows:

`spatial worker build --target=local --target=Windows`

- Deploy locally:

`spatial local launch {{launch_config}} --snapshot={{snapshot_file}}`

- Launch a local worker to connect to your local deployment:

`spatial local worker launch {{worker_type}} {{launch_config}}`

- Upload an assembly to use for cloud deployments:

`spatial cloud upload {{assembly_name}}`

- Launch a cloud deployment:

`spatial cloud launch {{assembly_name}} {{launch_config}} {{deployment_name}}`

- Clean worker directories:

`spatial worker clean`
