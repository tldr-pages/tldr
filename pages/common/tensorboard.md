# tensorboard

> Web-based visualization toolkit for inspecting and understanding machine learning experiments.
> More information: <https://www.tensorflow.org/tensorboard/get_started>.

- Start TensorBoard using the event files in a specific directory:

`tensorboard --logdir {{path/to/log_directory}}`

- Start TensorBoard on a specific port:

`tensorboard --logdir {{path/to/log_directory}} --port {{6006}}`

- Start TensorBoard and expose it to the local network:

`tensorboard --logdir {{path/to/log_directory}} --bind_all`

- Start TensorBoard with named runs from multiple log directories:

`tensorboard --logdir_spec {{name1}}:{{path/to/log_directory1}},{{name2}}:{{path/to/log_directory2}}`

- Reload log data at a specific interval (in seconds):

`tensorboard --logdir {{path/to/log_directory}} --reload_interval {{10}}`

- Print event file digests for debugging:

`tensorboard --inspect --logdir {{path/to/log_directory}}`

- Display help:

`tensorboard --help`

- Display version:

`tensorboard --version_tb`
