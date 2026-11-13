# dlt

> Create, inspect, and maintain data load tool (dlt) pipelines.
> More information: <https://dlthub.com/docs/reference/command-line-interface>.

- Create a pipeline project in the current directory from a verified source or a template:

`dlt init {{source}} {{destination}}`

- List the available sources or destinations:

`dlt init {{--list-sources|--list-destinations}}`

- List local pipelines:

`dlt pipeline {{[-l|--list-pipelines]}}`

- Display the state of a pipeline:

`dlt pipeline {{pipeline_name}} info`

- Display the trace of the last run of a pipeline:

`dlt pipeline {{pipeline_name}} trace`

- Display the failed jobs of a pipeline with their error messages:

`dlt pipeline {{pipeline_name}} failed-jobs`

- Display the default schema of a pipeline in a specific format:

`dlt pipeline {{pipeline_name}} schema --format {{json|yaml|dbml|dot|mermaid}}`

- Drop tables of specific resources and reset their state:

`dlt pipeline {{pipeline_name}} drop {{resource1 resource2 ...}}`
