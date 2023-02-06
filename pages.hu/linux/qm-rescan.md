# qm rescan

> Újravizsgálja az összes tárolót, és frissíti a virtuális gépek lemezméretét és a nem használt lemezképeket. További információ: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Egy adott virtuális gép összes tárolójának átvizsgálása, valamint a lemezméretek és a nem használt lemezképek frissítése:

`qm rescan {{vm_id}}`

- Végezze el az újraszkennelés szárazfutását egy adott virtuális gépen, és ne írjon semmilyen módosítást a konfigurációkba:

`qm rescan --dryrun {{true}} {{vm_id}}`
