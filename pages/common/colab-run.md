# colab run

> Run a Python script on a fresh Google Colab VM and automatically release it upon completion.
> More information: <https://github.com/googlecolab/google-colab-cli#execution>.

- Run a local script on a fresh CPU VM and release the VM upon completion:

`colab run {{path/to/script.py}}`

- Run a local script on a GPU runtime:

`colab run --gpu {{T4|L4|G4|A100|H100}} {{path/to/script.py}}`

- Run a local script on a TPU runtime:

`colab run --tpu {{v5e1|v6e1}} {{path/to/script.py}}`

- Run a script with forwarded command-line arguments:

`colab run {{path/to/script.py}} {{argument1 argument2 ...}}`

- Run a script on a GPU and keep the session active after completion:

`colab run --gpu {{T4|L4|G4|A100|H100}} --keep {{path/to/script.py}}`

- Run a script on a named session with a custom timeout:

`colab run {{[-s|--session]}} {{session_name}} --timeout {{60.0}} {{path/to/script.py}}`
