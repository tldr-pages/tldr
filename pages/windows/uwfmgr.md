# uwfmgr

> Unified Write Filter (UWF).
> Protect drives by redirecting any writes to the drive to a virtual overlay. Writes are discarded upon reboot unless committed by default.
> More information: <https://learn.microsoft.com/windows/iot/iot-enterprise/customize/unified-write-filter>.

- Get the current status:

`uwfmgr get-config`

- Set a drive as protected:

`uwfmgr volume protect {{drive_letter}}:`

- Remove a drive from protection list:

`uwfmgr volume unprotect {{drive_letter}}:`

- Enable or disable protection (Applies after reboot):

`uwfmgr filter {{enable|disable}}`

- Commit changes of a file on protected drive:

`uwfmgr file commit {{drive_letter:\path\to\file}}`

- Commit deletion of a file on protected drive:

`uwfmgr file commit-delete {{drive_letter:\path\to\file}}`
