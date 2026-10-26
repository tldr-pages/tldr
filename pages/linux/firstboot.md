# firstboot

> Reset OpenWrt to factory defaults by erasing settings and installed packages from the overlay.
> This command runs `factoryreset`.
> More information: <https://openwrt.org/docs/guide-user/troubleshooting/failsafe_and_factory_reset>.

- Ask for confirmation, then reset:

`firstboot`

- Assume [y]es and reset without asking:

`firstboot -y`

- Reset and [r]eboot:

`firstboot -r`

- Reset without asking, then reboot:

`firstboot -y -r`
