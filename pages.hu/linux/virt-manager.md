# virt-manager

> A virt-manager, a KVM és Xen virtuális gépek és LXC konténerek kezelésére szolgáló asztali felhasználói felület CLI indítója. További információ: <https://manpages.ubuntu.com/manpages/man1/virt-manager.1.html>.

- A virt-manager elindítása:

`virt-manager`

- Csatlakozás egy hypervisorhoz:

`virt-manager --connect {{hypervisor_uri}}`

- Ne forkolja a virt-manager folyamatot a háttérbe indításkor:

`virt-manager --no-fork`

- Hibakimenetek nyomtatása:

`virt-manager --debug`

- Nyissa meg az "Új VM" varázslót:

`virt-manager --show-domain-creator`

- Tartományi részletek ablak megjelenítése:

`virt-manager --show-domain-editor {{name|id|uuid}}`

- Tartomány teljesítmény ablak megjelenítése:

`virt-manager --show-domain-performance {{name|id|uuid}}`

- Kapcsolati részletek ablak megjelenítése:

`virt-manager --show-host-summary`
