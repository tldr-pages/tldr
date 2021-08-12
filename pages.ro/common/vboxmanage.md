# VBoxManage

> Interfață linie de comandă pentru VirtualBox.
> Include toate funcționalitățile GUI și multe altele.
> Mai multe informaţii: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-intro>

- Lista tuturor mașinilor virtuale VirtualBox:

`VBoxManage list vms`

- Afișați informații despre o anumită mașină virtuală:

`VBoxManage showvminfo {{name|uuid}}`

- Porniți o mașină virtuală:

`VBoxManage startvm {{name|uuid}}`

- Porniți o mașină virtuală în modul fără cap:

`VBoxManage startvm {{name|uuid}} -type headless`

- Opriți mașina virtuală și salvați starea curentă:

`VBoxManage controlvm {{name|uuid}} savestate`

- Închiderea mașinii virtuale fără a salva starea sa:

`VBoxManage controlvm {{name|uuid}} poweroff`

- Actualizare pachete de extensie vBox:

`VBoxManage extpack install --replace {{VboxExtensionPackFileName}}`
