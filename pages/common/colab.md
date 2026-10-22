# colab

> Command-line interface for Google Colab.
> Some subcommands such as `run` and `exec` have their own usage documentation.
> More information: <https://github.com/googlecolab/google-colab-cli#command-index>.

- Allocate a new named session with a specific GPU:

`colab new {{[-s|--session]}} {{session_name}} --gpu {{T4|L4|G4|A100|H100}}`

- List all active sessions:

`colab sessions`

- Run a local script on a fresh GPU VM and automatically release it upon completion:

`colab run --gpu {{T4|L4|A100|H100}} {{path/to/script.py}}`

- Execute a local Python script or Jupyter notebook in a specific session:

`colab exec {{[-s|--session]}} {{session_name}} {{[-f|--file]}} {{path/to/file.py|path/to/notebook.ipynb}}`

- Connect to an interactive TTY shell on the remote VM:

`colab console {{[-s|--session]}} {{session_name}}`

- Mount Google Drive in a specific session:

`colab drivemount {{[-s|--session]}} {{session_name}}`

- Download a file from the remote session:

`colab download {{[-s|--session]}} {{session_name}} {{path/to/remote_file}} {{path/to/local_destination}}`

- Stop and terminate a specific session:

`colab stop {{[-s|--session]}} {{session_name}}`
