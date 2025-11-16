# pio

> PlatformIO command-line interface for building, uploading, and managing embedded development projects.
> Some subcommands such as `run` have their own usage documentation.
> More information: <https://docs.platformio.org/en/latest/core/userguide/>.

- Initialize a new PlatformIO project:

`pio project init --board {{esp32dev}}`

- Build the project in the current directory:

`pio run`

- Upload firmware to the device:

`pio run {{[-t|--target]}} upload`

- Clean previous build files:

`pio run {{[-t|--target]}} clean`

- List detailed system information:

`pio system info`

- List supported boards for a platform:

`pio boards {{platform}}`

- Monitor the serial output:

`pio device monitor`

- Display the installed version of PlatformIO:

`pio --version`

