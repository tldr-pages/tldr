# Accelerate

> A library that enables the same PyTorch code to be run across any distributed configuration.
> More information: <https://huggingface.co/docs/accelerate/index>.

- Print environment information:

`accelerate env`

- Interactively create a configuration file:

`accelerate config`

- Print the estimated GPU memory cost of running a Hugging Face model with different data types:

`accelerate estimate-memory {{name/model}}`

- Test an Accelerate configuration file:

`accelerate test --config_file {{path/to/config.yaml}}`

- Run a model on CPU with Accelerate:

`accelerate launch {{path/to/script.py}} {{--cpu}}`

- Run a model on multi-GPU with Accelerate, with 2 machines:

`accelerate launch {{path/to/script.py}} --multi_gpu --num_machines 2`
