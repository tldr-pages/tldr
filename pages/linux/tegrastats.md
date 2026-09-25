# tegrastats

> Monitor memory usage and processor usage for NVIDIA Jetson-based devices.
> Note: Omitting `sudo` will leave out certain output.
> More information: <https://developer.nvidia.com/docs/drive/drive-os/7.0.3/public/drive-os-linux-sdk/development-workflow/NVIDIA_DRIVE_Utilities/tegrastats_Utility/tegrastatsOptions32.html>.

- Repeatedly print system statistics:

`sudo tegrastats`

- Set a custom interval in milliseconds:

`sudo tegrastats --interval {{1000}}`

- Write the output to a file:

`sudo tegrastats --logfile {{filename}}`
