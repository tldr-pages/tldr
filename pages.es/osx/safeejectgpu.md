# SafeEjectGPU

> Expulsa una GPU de forma segura.
> Más información: <https://keith.github.io/xcode-man-pages/SafeEjectGPU.8.html>.

- Expulsa todas las GPUs:

`SafeEjectGPU Eject`

- Lista todas las GPUs conectadas:

`SafeEjectGPU gpus`

- Lista de aplicaciones que utilizan una GPU:

`SafeEjectGPU gpuid {{gpu_id}} apps`

- Obtén el estado de una GPU:

`SafeEjectGPU gpuid {{gpu_id}} status`

- Expulsa una GPU:

`SafeEjectGPU gpuid {{gpu_id}} Eject`

- Inicia una aplicación en una GPU:

`SafeEjectGPU gpuid {{gpu_id}} LaunchOnGPU {{ruta/al/App.app}}`
