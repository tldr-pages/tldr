# mixxx

> Free and open source cross-platform DJ software.
> See also: `lmms`.
> More information: <https://manual.mixxx.org/2.5/en/chapters/appendix/commandline_dev_tools.html#command-line-options>.

- Start the Mixxx GUI in fullscreen:

`mixxx --fullScreen`

- Start in safe developer mode to debug a crash:

`mixxx --developer --safeMode`

- Debug a malfunction:

`mixxx --debugAssertBreak --developer --loglevel trace`

- Start Mixxx using the specified settings file:

`mixxx --resourcePath {{mixxx/res/controllers}} --settingsPath {{path/to/settings-file}}`

- Debug a custom controller mapping:

`mixxx --controllerDebug --resourcePath {{path/to/mapping-directory}}`

- Display help:

`mixxx --help`
