# acyclic

> Jadikan gambaran grafik berarah (dalam Graphviz) menjadi asiklik dengan memutarbalikkan beberapa garis tepi.
> Daftar filter Graphviz: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
> Informasi lebih lanjut: <https://graphviz.org/pdf/acyclic.1.pdf>.

- Ubah grafik berarah menjadi asiklik dengan membalikkan beberapa garis tepi:

`acyclic {{path/to/input.gv}} > {{path/to/output.gv}}`

- Cari tahu apakah grafik tersebut bersifat asiklik, memiliki siklus, atau tidak berarah, sehingga tidak menghasilkan output:

`acyclic -v -n {{path/to/input.gv}}`

- Tampilkan informasi bantuan untuk `acyclic`:

`acyclic -?`
