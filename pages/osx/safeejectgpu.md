# SafeEjectGPU

> Eject a GPU safely.
> More information: <https://keith.github.io/xcode-man-pages/SafeEjectGPU.8.html>.

- Eject all GPUs:

`SafeEjectGPU Eject`

- List all GPUs attached:

`SafeEjectGPU gpus`

- List apps using a GPU:

`SafeEjectGPU gpuid {{gpu_id}} apps`

- Get the status of a GPU:

`SafeEjectGPU gpuid {{gpu_id}} status`

- Eject a GPU:

`SafeEjectGPU gpuid {{gpu_id}} Eject`

- Launch an app on a GPU:

`SafeEjectGPU gpuid {{gpu_id}} LaunchOnGPU {{path/to/App.app}}`
