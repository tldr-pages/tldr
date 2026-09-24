# slmgr.vbs

> Install, activate, and manage Windows licenses.
> Use `cscript` to run this program as a CLI, or `wscript` as a GUI.
> Note: This command may override, deactivate, and/or remove your current Windows license, so please proceed cautiously.
> More information: <https://learn.microsoft.com/windows-server/get-started/activation-slmgr-vbs-options>.

- [d]isplay the current Windows [l]icense [i]nformation:

`cscript slmgr.vbs /dli`

- [d]isplay the ins[t]allation [i]D for the current device. Useful for offline license activation:

`cscript slmgr.vbs /dti`

- Display the current license's e[xp]i[r]ation date and time:

`cscript slmgr.vbs /xpr`

- [i]nstall a new Windows license [p]roduct [k]ey. Requires Administrator privileges and will override the existing license:

`cscript slmgr.vbs /ipk {{product_key}}`

- [a]c[t]ivate the Windows product license [o]nline. Requires Administrator privileges to do so:

`cscript slmgr.vbs /ato`

- [a]c[t]ivate the Windows [p]roduct license offline. Requires Administrator privileges and a Confirmation ID provided by Microsoft Product Activation Center:

`cscript slmgr.vbs /atp {{confirmation_id}}`

- [c]lear the current license's [p]roduct [k]e[y] from the Windows Registry. This will not deactivate or uninstall the current license, but prevents the key from being stolen by malicious programs in the future:

`cscript slmgr.vbs /cpky`

- [u]ninstall the current license (by its [p]roduct [k]ey):

`cscript slmgr.vbs /upk`
