# ollama

> A large language model runner.
> More information: <https://github.com/jmorganca/ollama>.

- Start the daemon required to run other commands:

`ollama serve`

- Run a model:

`ollama run {{model}}`

- List downloaded models:

`ollama list`

- Delete a model:

`ollama rm {{model}}`

- Create a model from a `Modelfile`:

`ollama create {{new_model_name}} -f {{path/to/file}}`
