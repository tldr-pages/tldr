# quarkus

> Create Quarkus projects, manage extensions and perform essential build and development tasks.
> More information: <https://quarkus.io/guides/cli-tooling>.

- Create a new application project in a new directory:

`quarkus create app {{project_name}}`

- Run the current project in live coding mode:

`quarkus dev`

- Run the application:

`quarkus run`

- Run the current project in continuous testing mode:

`quarkus test`

- Add one or more extensions to the current project:

`quarkus extension add {{extension_name1 extension_name2 ...}}`

- Build a container image using Docker:

`quarkus image build docker`

- Deploy the application to Kubernetes:

`quarkus deploy kubernetes`

- Update project:

`quarkus update`
