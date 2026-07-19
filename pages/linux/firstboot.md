# firstboot

> Reset an OpenWrt device to factory defaults by wiping the overlay filesystem.
> See also: `sysupgrade`.
> More information: <https://openwrt.org/docs/guide-user/troubleshooting/failsafe_and_factory_reset>.

- Reset configuration to factory defaults (prompts for confirmation):

`firstboot`

- Reset without prompting for confirmation:

`firstboot -y`

- Reset to factory defaults, then restart the device:

`firstboot -y && reboot`
