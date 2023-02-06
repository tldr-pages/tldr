# virt-viewer

> Minimális grafikus felület egy virtuális géphez (VM). MEGJEGYZÉS: a "domain" a meglévő VM-ek nevére, UUID-jára vagy azonosítójára utal (Lásd: tldr virsh). További információ: <https://manned.org/virt-viewer>.

- A `virt-viewer` indítása a futó virtuális gépek kiválasztására szolgáló kéréssel:

`virt-viewer`

- A `virt-viewer` elindítása egy adott virtuális géphez ID, UUID vagy név alapján:

`virt-viewer "{{domain}}"`

- Várjon egy virtuális gép indítására, és automatikusan csatlakozzon újra, ha az leállt és újraindul:

`virt-viewer --reconnect --wait "{{domain}}"`

- Csatlakozás egy adott távoli virtuális géphez TLS-en keresztül:

`virt-viewer --connect "xen//{{url}}" "{{domain}}"`

- Csatlakozás egy adott távoli virtuális géphez SSH-n keresztül:

`virt-viewer --connect "qemu+ssh//{{username}}@{{url}}/system" "{{domain}}"`
