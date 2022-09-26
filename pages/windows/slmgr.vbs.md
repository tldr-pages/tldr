# slmgr.vbs

> Install, activate, and manage Windows licenses.
> This command may override, deactivate, and/or remove your current Windows license. Please proceed with caution.
> More information: <https://docs.microsoft.com/windows-server/get-started/activation-slmgr-vbs-options>.

- [d]isplay the current Windows [l]icense [i]nformation:

`slmgr /dli`

- [d]isplay the ins[t]allation [i]D for the current device. Useful for offline license activation:

`slmgr /dti`

- Display the current license's e[xp]i[r]ation date and time:

`slmgr /xpr`

- [i]nstall a new Windows license [p]roduct [k]ey. Requires Administrator privileges and will override the existing license:

`slmgr /ipk {{product_key}}`

- [a]c[t]ivate the Windows product license [o]nline. Requires Administrator privileges to do so:

`slmgr /ato`

- [a]c[t]ivate the Windows [p]roduct license offline. Requires Administrator privileges and an Confirmation ID provided by Microsoft Product Activation Center:

`slmgr /atp {{confirmation_id}}`

- [c]lear the current license's [p]roduct [k]e[y] from the Windows Registry. This will not deactivate or uninstall the current license, but prevents the key from being stolen by malicious programs in the future:

`slmgr /cpky`

- [u]ninstall the current license (by its [p]roduct [k]ey):

`slmgr /upk`
