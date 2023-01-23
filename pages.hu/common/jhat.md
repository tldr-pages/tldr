# jhat

> Java heap elemző eszköz. További információ: <https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jhat.html>.

- A heap dump elemzése (a `jmap` oldalról), megtekintés HTTP-n keresztül a 7000-es porton:

`jhat {{dump_file.bin}}`

- Heap dump elemzése, a http-kiszolgáló alternatív portjának megadásával:

`jhat -p {{port}} {{dump_file.bin}}`

- Elemezzen egy dumpot, amely lehetővé teszi a `jhat` számára, hogy legfeljebb 8 GB RAM-ot használjon (2-4x dump mérete ajánlott):

`jhat -J-mx8G {{dump_file.bin}}`
