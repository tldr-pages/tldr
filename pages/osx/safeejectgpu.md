# SafeEjectGPU

> Eject a GPU safely.
> More information: <https://www.unix.com/man-page/mojave/8/safeejectgpu>.

- Eject all GPUs:

`SafeEjectGPU Eject`

- List all GPUs attached:

`SafeEjectGPU gpus`

- List apps using a GPU:

`SafeEjectGPU gpuid {{GPU_ID}} apps`

- Get the status of a GPU:

`SafeEjectGPU gpuid {{GPU_ID}} status`

- Eject a GPU:

`SafeEjectGPU gpuid {{GPU_ID}} Eject`

- Launch an app on a GPU:

`SafeEjectGPU gpuid {{GPU_ID}} LaunchOnGPU {{path/to/App.app}}`
