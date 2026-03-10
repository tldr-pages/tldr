# owut

> OpenWrt Upgrade Tool for automating builds and installs via Attended SysUpgrade (ASU).
> More information: <https://openwrt.org/docs/guide-user/installation/sysupgrade.owut>.

- List available OpenWrt versions for the current device:

`owut versions`

- List user installed or removed packages:

`owut list`

- Check for updates without performing an upgrade:

`owut check`

- Automatically build, download, verify, and install the latest available firmware:

`owut upgrade`

- Upgrade to a specific version and include additional packages:

`owut upgrade {{[-V|--version-to]}} {{version}} {{[-a|--add]}} "{{htop vim}}"`

- Download and verify a specific image without installing it:

`owut download {{[-V|--version-to]}} {{25.12.0}}`

- Verify the latest downloaded image and install it:

`owut install`
