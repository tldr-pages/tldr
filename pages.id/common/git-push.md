# git push

> Dorong kumpulan komit menuju suatu repositori jarak jauh (remote).
> Informasi lebih lanjut: <https://git-scm.com/docs/git-push>.

- Kirim perubahan lokal dari cabang (branch) saat ini menuju cabang yang sepadan pada repositori tujuan:

`git push`

- Kirim perubahan dari cabang lokal yang ditentukan menuju cabang yang sepadan pada repositori tujuan:

`git push {{nama_remote}} {{cabang_lokal}}`

- Kirim perubahan dari cabang lokal yang ditentukan menuju cabang sepadan pada repositori tujuan, dan simpan remote sebagai target operasi dorong (push) dan tarik (pull) bagi cabang lokal tersebut:

`git push {{[-u|--set-upstream]}} {{nama_remote}} {{cabang_lokal}}`

- Kirim perubahan dari suatu cabang lokal menuju suatu cabang remote secara spesifik:

`git push {{nama_remote}} {{cabang_lokal}}:{{cabang_remote}}`

- Kirim perubahan dari setiap cabang lokal menuju cabang-cabang sepadan dalam repositori tujuan:

`git push --all {{nama-remote}}`

- Hapus suatu cabang dalam suatu repositori remote:

`git push {{nama_remote}} {{[-d|--delete]}} {{cabang_remote}}`

- Hapus cabang-cabang remote yang tidak memiliki padanan pada repositori lokal:

`git push --prune {{nama_remote}}`

- Publikasikan kumpulan tag komit yang belum dipublikasikan dalam repositori remote:

`git push --tags`
