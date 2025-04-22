# sbctl

> A user-friendly secure boot key manager.
> Note: Not enrolling Microsoft's certificates can brick your system. See <https://github.com/Foxboron/sbctl/wiki/FAQ#option-rom>.
> More information: <https://github.com/Foxboron/sbctl#usage>.

- Show the current secure boot status:

`sbctl status`

- Create custom secure boot keys (by default, everything is stored in `/var/lib/sbctl`):

`sbctl create-keys`

- Enroll the custom secure boot keys and Microsoft's UEFI vendor certificates:

`sbctl enroll-keys --microsoft`

- Automatically run `create-keys` and `enroll-keys` based on the settings in `/etc/sbctl/sbctl.conf`:

`sbctl setup --setup`

- Sign an EFI binary with the created key and save the file to the database:

`sbctl sign {{[-s|--save]}} {{path/to/efi_binary}}`

- Re-sign all the saved files:

`sbctl sign-all`

- Verify that all EFI executables on the EFI system partition have been signed:

`sbctl verify`
