brltty

Start the brltty daemon to provide access to the console for users of refreshable braille displays.

- `brltty`
  Start the brltty daemon (auto-detect device and backend).

- `brltty -b al -d /dev/ttyUSB0`
  Start brltty using backend `al` and device `/dev/ttyUSB0` (replace with your backend/device).

- `brltty --preferences`
  List available settings and preferences.

- `brltty --help`
  Show help and available command-line options.

- `brltty --version`
  Show version information.

- `pkill brltty`
  Stop the running brltty daemon.

> More information: https://brltty.app/doc/Handbook.html
