# SafeEjectGPU

> Eject a GPU safely.
> More information: <https://ss64.com/osx/safeejectgpu.html>.

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
