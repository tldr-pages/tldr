# SafeEjectGPU

> Expulsa una GPU de forma segura.
> Más información: <https://www.unix.com/man-page/mojave/8/safeejectgpu>.

- Expulsa todas las GPUs:

`SafeEjectGPU Eject`

- Lista todas las GPUs conectadas:

`SafeEjectGPU gpus`

- Lista de aplicaciones que utilizan una GPU:

`SafeEjectGPU gpuid {{GPU_ID}} apps`

- Obtiene el estado de una GPU:

`SafeEjectGPU gpuid {{GPU_ID}} status`

- Expulsa una GPU:

`SafeEjectGPU gpuid {{GPU_ID}} Eject`

- Inicia una aplicación en una GPU:

`SafeEjectGPU gpuid {{GPU_ID}} LaunchOnGPU {{ruta/al/App.app}}`
