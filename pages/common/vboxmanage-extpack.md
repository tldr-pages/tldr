# vboxmanage-extpack

> Manage extension packs for Oracle VirtualBox.
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-extpack>.

- Install extension packs to VirtualBox (Note: you need to remove the existing version of the extension pack before installing a new version.):

`VBoxManage extpack install {{path/to/file.vbox-extpack}}`

- Remove the existing version of the VirtualBox extension pack:

`VBoxManage extpack install --replace`

- Uninstall extension packs from VirtualBox:

`VBoxManage extpack uninstall {{extension_pack_name}}`

- Uninstall extension packs and skip most uninstallation refusals:

`VBoxManage extpack uninstall --force {{extension_pack_name}}`

- Clean up temporary files and directories left by extension packs:

`VBoxManage extpack cleanup`
