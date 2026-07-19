# jffs2reset

> Reset the OpenWrt overlay filesystem to factory defaults.
> See also: `firstboot`, `sysupgrade`.
> More information: <https://openwrt.org/docs/guide-user/troubleshooting/failsafe_and_factory_reset>.

- Reset the overlay filesystem (prompts for confirmation):

`jffs2reset`

- Reset without prompting for confirmation:

`jffs2reset -y`

- Reset the overlay, then restart the device:

`jffs2reset -y && reboot`
