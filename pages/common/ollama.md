# ollama

> A large language model runner.
> More information: <https://github.com/jmorganca/ollama>.

- Start the daemon required to run other commands:

`ollama serve`

- Run a model and chat with it:

`ollama run {{model}}`

- Run a model with a single prompt:

`ollama run {{model}} {{prompt}}`

- List downloaded models:

`ollama list`

- Delete a model:

`ollama rm {{model}}`

- Create a model from a `Modelfile`:

`ollama create {{new_model_name}} -f {{path/to/Modelfile}}`
