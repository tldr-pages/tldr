# SafeEjectGPU

> Eject a GPU safely.
> Visit the man page for more info.

- Eject all GPUs:

`SafeEjectGPU Eject`

- List all GPUs attached:

`SafeEjectGPU gpus`

- List apps using a specified GPU:

`SafeEjectGPU gpuid {{GPU_ID}} apps`

- Get the status of a specified GPU:

`SafeEjectGPU gpuid {{GPU_ID}} status`

- Eject a specified GPU:

`SafeEjectGPU gpuid {{GPU_ID}} Eject`

- Launch an app on a specified GPU:

`SafeEjectGPU gpuid {{GPU_ID}} LaunchOnGPU {{path/to/App.app}}`
