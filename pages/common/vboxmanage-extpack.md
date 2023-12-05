# vboxmanage-extpack

> Manage extension packs for Oracle VirtualBox.
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-import>.

- Install extension packs to VirtualBox:

`VBoxManage extpack install {{VboxExtensionPackFileName}}`

- Update VBox extension packs:

`VBoxManage extpack install --replace {{VboxExtensionPackFileName}}`

- Uninstall extension packs from VirtualBox:

`VBoxManage extpack uninstall {{VboxExtensionPackFileName}}`

- Uninstall extension packs and skip most uninstallation refusal:

`VBoxManage extpack uninstall --force {{VboxExtensionPackFileName}}`

- Clean up temporary file and directory left by extension packs:

`VBoxManage extpack cleanup`
