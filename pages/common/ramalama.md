# ramalama

> Manager for large language models.
> More information: <https://github.com/containers/ramalama#Commands>.

- Pull a model from a remote registry:

`ramalama pull {{model}}`

- Remove a model from local storage:

`ramalama rm {{model}}`

- Run a model as a chatbot:

`ramalama run {{model}}`

- Serve a REST API on a model:

`ramalama serve {{model}}`

- List all RamaLama containers:

`ramalama containers`

- List all downloaded models:

`ramalama list`

- Stop a container that is running a model:

`ramalama stop {{model}}`

- Push a local model to a remote registry:

`ramalama push {{registry_url}}`
