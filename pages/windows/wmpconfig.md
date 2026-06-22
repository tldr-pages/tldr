# wmpconfig

> Manage network sharing for Windows Media Player (legacy).
> Note: This command requires administrator privileges.
> See also: `wmpnscfg`.
> More information: <https://learn.microsoft.com/previous-versions/windows/desktop/wmp/command-line-parameters>.

- Turn network sharing on or off:

`wmpconfig {{HMEOn|HMEOff}}`

- Stop a specific network device from sharing to this computer using its MAC address:

`wmpconfig DisableHMEDevice {{mac_address}}`

- Remove a network device from sharing to this computer:

`wmpconfig RemoveHMEDevice {{mac_address}}`

- Restore a network device from sharing to this computer:

`wmpconfig RestoreHMEDevice {{mac_address}}`

- Set the parental control level for playing DVD content:

`wmpconfig SetDVDParentalLevel {{3}}`
