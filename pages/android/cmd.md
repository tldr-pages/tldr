# cmd

> Android service manager.
> More information: <https://cs.android.com/android/platform/superproject/+/master:frameworks/native/cmds/cmd/>.

- List every running service:

`cmd -l`

- Call a specific service:

`cmd {{alarm}}`

- Call a service with arguments:

`cmd {{vibrator}} {{vibrate 300}}`
