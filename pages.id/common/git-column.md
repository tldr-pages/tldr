# git column

> Tampilkan data dalam bentuk kolom.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-column>.

- Tampilkan `stdin` dalam bentuk beberapa kolom:

`ls | git column --mode={{column}}`

- Tampilkan `stdin` sebagai beberapa kolom dengan lebar maksimum sebesar `100`:

`ls | git column --mode=column --width={{100}}`

- Tampilkan `stdin` sebagai beberapa kolom dengan padding maksimum sebesar `30`:

`ls | git column --mode=column --padding={{30}}`
