# fdisk

> A merevlemezen lévő partíciós táblák és partíciók kezelésére szolgáló program. Lásd még: `partprobe`. További információ: <https://manned.org/fdisk>.

- Partíciók listázása:

`sudo fdisk -l`

- A partíciókezelő elindítása:

`sudo fdisk {{/dev/sdX}}`

- A lemez particionálása után hozzon létre egy partíciót:

`n`

- A lemez particionálása után válasszon ki egy partíciót a törléshez:

`d`

- Egy lemez particionálása után tekintse meg a partíciós táblázatot:

`p`

- A lemez particionálása után írja ki a végrehajtott változtatásokat:

`w`

- A lemez particionálása után a végrehajtott változtatások elvetése:

`q`

- A lemez particionálása után megnyithatja a súgó menüt:

`m`
