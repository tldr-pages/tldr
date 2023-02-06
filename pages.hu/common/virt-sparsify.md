# virt-sparsify

> A virtuális gépek meghajtó képeit vékonyan rendelkezésre bocsátottá teszi. MEGJEGYZÉS: Csak offline gépekhez használja az adatok sérülésének elkerülése érdekében. További információ: <https://libguestfs.org>.

- Létrehozhat egy szűkített tömörített képet pillanatképek nélkül egy szűkítetlen képből:

`virt-sparsify --compress {{path/to/image.qcow2}} {{path/to/image_new.qcow2}}`

- Helyben ritkít egy képet:

`virt-sparsify --in-place {{path/to/image.img}}`
