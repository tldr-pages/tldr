# slmgr

> Install, activate, and manage Windows licenses.
> This command may override, deactivate, and/or remove your current Windows license. Please proceed with caution.
> More information: <https://docs.microsoft.com/windows-server/get-started/activation-slmgr-vbs-options>.

- [D]isplay the current Windows [l]icense [i]nformation:

`slmgr /dli`

- [D]isplays the ins[t]allation [I]D for the current device. Useful for offline license activation:

`slmgr /dti`

- Display the current license's e[xp]i[r]ation date and time:

`slmgr /xpr`

- [I]nstalls a new Windows license [p]roduct [k]ey. Requires Administrator priviledges and will override your existing license:

`slmgr /ipk`

- [A]c[t]ivate the Windows product license [o]nline. Requires Administrator priviledges to do so:

`slmgr /ato`

- [A]c[t]ivate the Windows [p]roduct license offline. Requires Administrator priviledges and an Confirmation ID provided by Microsoft Product Activation Center:

`slmgr /atp {{confirmation_id}}`

- [C]lears the current license's [p]roduct [k]e[y] from the Windows Registry. This will not deactivate or uninstall the current license, but prevent the key from being stolen by malicious programs in the future:

`slmgr /cpky`

- [U]ninstall the current license (by its [p]roduct [k]ey):

`slmgr /upk`
