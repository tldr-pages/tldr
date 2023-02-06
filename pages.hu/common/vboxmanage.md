# VBoxManage

> A VirtualBox parancssori interfésze, amely tartalmazza a GUI összes funkcióját és még többet is. További információ: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-intro>.

- Az összes VirtualBox virtuális gép listázása:

`VBoxManage list vms`

- Információk megjelenítése egy adott virtuális gépről:

`VBoxManage showvminfo {{name|uuid}}`

- Virtuális gép indítása:

`VBoxManage startvm {{name|uuid}}`

- Virtuális gép indítása fej nélküli üzemmódban:

`VBoxManage startvm {{name|uuid}} --type headless`

- A virtuális gép leállítása és aktuális állapotának mentése:

`VBoxManage controlvm {{name|uuid}} savestate`

- A virtuális gép leállítása állapotának mentése nélkül:

`VBoxManage controlvm {{name|uuid}} poweroff`

- VBox bővítménycsomagok frissítése:

`VBoxManage extpack install --replace {{VboxExtensionPackFileName}}`
