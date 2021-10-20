# wdctl

> Shoes hardware watchdog status.
> The Linux kernel can reset the system if serious problems are detected. This can be implemented via special watchdog hardware, or via a slightly less reliable software-only watchdog inside the kernel.
> More information: <https://man7.org/linux/man-pages/man8/wdctl.8.html>.

- Display watchdog status:

`wdctl`

- Display watchdog status on a single line (`key=value` pairs):

`wdctl --oneline`

- Display only some watchdog flags (list is driver specific):

`wdctl --flags {{flag list}}`
