# nvtop

> Neat Videocard TOP: an htop-like monitor for GPUs and accelerators.
> See also: `amdgpu_top`, `radeontop`.
> More information: <https://github.com/Syllo/nvtop>.

- Launch the interactive GPU monitor:

`nvtop`

- Monitor GPUs using a specific vendor backend (when multiple are available):

`nvtop --vendor {{nvidia|amd|intel}}`

- Start with a specific GPU selected:

`nvtop --gpu {{0}}`

- Change the update interval in seconds:

`nvtop --update-interval {{2}}`

- Open the interactive setup window to customize the UI:

`nvtop`
