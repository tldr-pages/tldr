# rm

> Șterge fișiere sau foldere.
> Vezi și: `rmdir`, `trash`.
> Mai multe informații: <https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html>.

- Șterge fișiere specifice:

`rm {{cale/către/fișier1 cale/către/fișier2 ...}}`

- Șterge fișiere specifice ignorând cele care nu există:

`rm {{[-f|--force]}} {{cale/către/fișier1 cale/către/fișier2 ...}}`

- Șterge fișiere specifice cerând confirmare interactiv înainte de fiecare ștergere:

`rm {{[-i|--interactive]}} {{cale/către/fișier1 cale/către/fișier2 ...}}`

- Șterge fișiere specifice afișând informații despre fiecare ștergere:

`rm {{[-v|--verbose]}} {{cale/către/fișier1 cale/către/fișier2 ...}}`

- Șterge recursiv fișiere și foldere specifice:

`rm {{[-r|--recursive]}} {{cale/către/fișier_sau_folder1 cale/către/fișier_sau_folder2 ...}}`

- Șterge folderele goale (aceasta este considerată metoda sigură):

`rm {{[-d|--dir]}} {{cale/către/folder}}`
