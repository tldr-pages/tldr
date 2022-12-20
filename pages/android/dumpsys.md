# dumpsys

> Provide information about Android system services.
> This command can only be used through `adb shell`.
> More information: <https://developer.android.com/studio/command-line/dumpsys>.

- Display diagnostic output for all system services:

`dumpsys`

- Display diagnostic output for a specific system service:

`dumpsys {{service}}`

- [l]ist all services:

`dumpsys -l`

- List service-specific arguments for a service:

`dumpsys {{service}} -h`

- Exclude a specific service from the diagnostic output:

`dumpsys --skip {{service}}`

- Specify a [t]imeout period in seconds (`-t` default: 10s):

`dumpsys -t {{1..infinity}}`
