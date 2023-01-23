# SafeEjectGPU

> A GPU biztonságos kivetítése. További információ: <https://www.unix.com/man-page/mojave/8/safeejectgpu>.

- Dobja ki az összes GPU-t:

`SafeEjectGPU Eject`

- Az összes csatlakoztatott GPU listázása:

`SafeEjectGPU gpus`

- GPU-t használó alkalmazások listázása:

`SafeEjectGPU gpuid {{GPU_ID}} apps`

- A GPU állapotának lekérdezése:

`SafeEjectGPU gpuid {{GPU_ID}} status`

- GPU-k kidobása:

`SafeEjectGPU gpuid {{GPU_ID}} Eject`

- Alkalmazás indítása GPU-n:

`SafeEjectGPU gpuid {{GPU_ID}} LaunchOnGPU {{path/to/App.app}}`
