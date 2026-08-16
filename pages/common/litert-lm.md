# litert-lm

> CLI tool for running and managing LiteRT-LM models.
> More information: <https://developers.google.com/edge/litert-lm/cli/usage>.

- List all imported models:

`litert-lm list`

- Run a local or imported model interactively:

`litert-lm run {{path/to/model.litertlm|model_id}}`

- Run a model directly from a Hugging Face repository with a single prompt:

`litert-lm run --from-huggingface-repo {{owner/repository}} {{model.litertlm}} --prompt "{{What is the capital of France?}}"`

- Run a model using GPU acceleration:

`litert-lm run {{path/to/model.litertlm|model_id}} --backend gpu`

- Run a multimodal model with an image attachment:

`litert-lm run {{path/to/model.litertlm|model_id}} --vision-backend {{gpu|cpu}} --attachment {{path/to/image.jpg}} --prompt "{{Describe this image.}}"`

- Run a model with Python function calling tools via a preset file:

`litert-lm run {{path/to/model.litertlm|model_id}} --preset {{path/to/preset.py}}`

- Benchmark a model's performance:

`litert-lm benchmark {{path/to/model.litertlm|model_id}}`

- Start an OpenAI-compatible API server on a specific port:

`litert-lm serve --port {{9379}}`
