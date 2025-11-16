# pio

> PlatformIO command-line interface for building, uploading, and managing embedded development projects.
> More information: <https://docs.platformio.org>.

- Initialize a new PlatformIO project in the current directory:

`pio project init`

- Build the project (compile source files):

`pio run`

- Upload firmware to the connected board as defined in `platformio.ini`:

`pio run --target upload`

- Clean previous build files:

`pio run --target clean`

- Open the PlatformIO Serial Monitor:

`pio device monitor`

- List all available development boards:

`pio boards`

- List installed and available platforms:

`pio platform list`

