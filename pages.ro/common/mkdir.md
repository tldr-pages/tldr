# mkdir

> Creează foldere și le setează permisiunile.
> Mai multe informații: <https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html>.

- Creează foldere specifice:

`mkdir {{cale/către/folder1 cale/către/folder2 ...}}`

- Creează foldere specifice și folderele părinte dacă este nevoie:

`mkdir {{[-p|--parents]}} {{cale/către/folder1 cale/către/folder2 ...}}`

- Creează foldere cu permisiuni specifice:

`mkdir {{[-m|--mode]}} {{rwxrw-r--}} {{cale/către/folder1 cale/către/folder2 ...}}`

- Creează mai multe foldere imbricate, recursiv:

`mkdir {{[-p|--parents]}} {{cale/către/{a,b}/{x,y,z}/{h,i,j}}}`
