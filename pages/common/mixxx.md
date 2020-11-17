# mixxx

> Free and open source cross-platform DJ software.
> More information: <https://mixxx.org/manual/latest/chapters/appendix.html#command-line-options>.

- Start the Mixxx GUI in full-screen:

`mixxx --fullScreen`

- Start in safe developer mode to debug a crash:

`mixxx --developer --safeMode`

- Debug a malfunction:

`mixxx --debugAssertBreak --developer --loglevel trace`

- Start mixxx using a contained configuration:

`mixxx --resourcePath {{mixxx/res/controllers}} --settingsPath {{settingsPath}}`

- Debug a custom controller mapping:

`mixxx --controllerDebug --resourcePath {{custom/mapping/directory}}`

- Show command-line help:

`mixxx --help`
