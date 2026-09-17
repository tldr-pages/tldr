# ollama

> A large language model runner.
> For a list of available models, see <https://ollama.com/library>.
> More information: <https://docs.ollama.com/cli>.

- Start the daemon required to run other commands:

`ollama serve`

- Run a model and chat with it (will automatically download the model if it's not downloaded):

`ollama run {{model}}`

- Run a model with a single prompt and thinking turned off:

`ollama run {{model}} --think=false "{{prompt}}"`

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
