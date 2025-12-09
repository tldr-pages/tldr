# lvmsar

> LVM system activity reporter.
> Not supported under LVM2; prefer `dmstats`.
> More information: <https://manned.org/lvmsar>.

- Run the legacy reporter (LVM1 systems only):

`lvmsar`

- Report I/O statistics for a device using device-mapper stats:

`dmstats report {{/dev/mapper/device}}`

- List statistics regions for a device:

`dmstats list {{/dev/mapper/device}}`
