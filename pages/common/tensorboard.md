# tensorboard

> Web-based visualization toolkit for inspecting and understanding machine learning experiments.
> More information: <https://www.tensorflow.org/tensorboard>.

- Start TensorBoard using the event files in a specific directory:

`tensorboard --logdir {{path/to/logdir}}`

- Start TensorBoard on a specific port:

`tensorboard --logdir {{path/to/logdir}} --port {{6006}}`

- Start TensorBoard and expose it to the local network:

`tensorboard --logdir {{path/to/logdir}} --bind_all`

- Start TensorBoard with named runs from multiple log directories:

`tensorboard --logdir_spec {{name1:path/to/logs/1,name2:path/to/logs/2}}`

- Reload log data every 10 seconds:

`tensorboard --logdir {{path/to/logdir}} --reload_interval {{10}}`

- Print event file digests for debugging:

`tensorboard --inspect --logdir {{path/to/logdir}}`

- Display help:

`tensorboard --help`

- Display version:

`tensorboard --version_tb`
