# Accelerate

> 🤗 Accelerate is a library that enables the same PyTorch code to be run across any distributed configuration by adding just four lines of code!
> In short, training and inference at scale made simple, efficient and adaptable.
> More information: <https://huggingface.co/docs/accelerate/index>.

- Print environment information:

`accelerate env`

- Interactively set `default_config.yaml` config:

`accelerate config`

- Print estimated GPU memory cost of a huggingface model with different data types:

`accelerate estimate-memory {{name/model}}`

- Test an Accelerate configuration file:

`accelerate test --config_file {{path_to_config.yaml}}`

- Run a model on CPU with Accelerate:

`accelerate launch {{path/to/script.py}} {{--cpu}}`

- Run a model on multi-GPU with Accelerate, with 2 machines:

`accelerate launch {{path/to/script.py}} --multi_gpu --num_machines {{2}}`
