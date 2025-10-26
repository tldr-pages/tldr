# mhwd-gpu

> Configure graphics cards in Manjaro.
> More information: <https://wiki.manjaro.org/index.php/Configure_NVIDIA_(non-free)_settings_and_load_them_on_Startup/en#Configure_The_Resolution.2FRefresh_Rate>.

- Show current Xorg configuration path:

`mhwd-gpu --status`

- Check if Xorg configuration has a valid symlink:

`mhwd-gpu --check`

- Set a custom Xorg configuration for an Nvidia GPU:

`sudo mhwd-gpu --setmod nvidia --setxorg /{{path/to/nvidia.conf}}`

- Set a custom Xorg configuration for an AMD GPU:

`sudo mhwd-gpu --setmod {{catalyst|ati}} --setxorg /{{path/to/amdgpu.conf}}`

- Display help:

`mhwd-gpu --help`
