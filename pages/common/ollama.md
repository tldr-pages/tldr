# ollama

> A large language model runner.
> For a list of available models, see <https://ollama.com/library>.
> More information: <https://github.com/ollama/ollama>.

- Start the daemon required to run other commands:

`ollama serve`

- Run a model and chat with it:

`ollama run {{model}}`

- Run a model with a single prompt:

`ollama run {{model}} {{prompt}}`

- List downloaded models:

`ollama {{[ls|list]}}`

- Pull a specific model:

`ollama pull {{model}}`

- List running models:

`ollama ps`

- Delete a model:

`ollama rm {{model}}`

- Create a model from a `Modelfile`:

`ollama create {{new_model_name}} {{[-f|--file]}} {{path/to/Modelfile}}`
