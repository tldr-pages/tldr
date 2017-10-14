# fly

> Cli tool for concourse-ci.

- Authenticating with and saving concourse target:

`fly --target {{example}} login --team-name {{my-team}} -c {{https://ci.example.com}}`

- List targets:

`fly targets`

- List pipelines:

`fly -t {{example}} pipelines`

- Configure pipeline:

`fly -t {{example}} set-pipeline --config {{pipeline.yml}} --pipeline {{my-pipeline}}`

- Unpause pipeline:

`fly -t {{example}} unpause-pipeline --pipeline {{my-pipeline}}`

- Show pipeline configuration:

`fly -t {{example}} get-pipeline --pipeline {{my-pipeline}}`

- Update local copy of fly:

`fly -t {{example}} sync`

- Destroy pipeline:

`fly -t {{example}} destroy-pipeline --pipeline {{my-pipeline}}`
