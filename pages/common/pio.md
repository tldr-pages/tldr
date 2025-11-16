# pio

> Development environment for embedded boards.
> Build, upload, and manage embedded development projects.
> More information: <https://docs.platformio.org/en/latest/core/userguide/>.

- Display version:
`pio --version`

- Initialize a new PlatformIO project for a specific board:
`pio project init {{[-b|--board]}} {{esp32dev}}`

- Build the project in the current directory:
`pio run`

- Upload firmware to the connected board:
`pio run {{[-t|--target]}} upload`

- Clean previous build files:
`pio run {{[-t|--target]}} clean`

- List supported boards for a platform:
`pio boards {{platform}}`

- Monitor the serial output of the device:
`pio device monitor`
