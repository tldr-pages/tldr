# fly

> Command-line tool for concourse-ci.
> More information: <https://concourse-ci.org/fly.html>.

- Authenticate with and save concourse target:

`fly {{[-t|--target]}} {{target_name}} login {{[-n|--team-name]}} {{team_name}} {{[-c|--concourse-url]}} {{https://ci.example.com}}`

- List targets:

`fly targets`

- List pipelines:

`fly {{[-t|--target]}} {{target_name}} pipelines`

- Upload or update a pipeline:

`fly {{[-t|--target]}} {{target_name}} set-pipeline {{[-c|--config]}} {{pipeline.yml}} {{[-p|--pipeline]}} {{pipeline_name}}`

- Unpause pipeline:

`fly {{[-t|--target]}} {{target_name}} unpause-pipeline {{[-p|--pipeline]}} {{pipeline_name}}`

- Show pipeline configuration:

`fly {{[-t|--target]}} {{target_name}} get-pipeline {{[-p|--pipeline]}} {{pipeline_name}}`

- Update local copy of fly:

`fly {{[-t|--target]}} {{target_name}} sync`

- Destroy pipeline:

`fly {{[-t|--target]}} {{target_name}} destroy-pipeline {{[-p|--pipeline]}} {{pipeline_name}}`
