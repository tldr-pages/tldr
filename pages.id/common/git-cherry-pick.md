# git cherry-pick

> Lakukan perubahan yang tercatat pada komit-komit saat ini menuju cabang saat ini.
> Gunakan `git checkout` terlebih dahulu jika hendak melakukan perubahan pada cabang lainnya.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-cherry-pick>.

- Lakukan perubahan menurut suatu komit terhadap cabang saat ini:

`git cherry-pick {{komit}}`

- Lakukan perubahan berdasarkan urutan komit terhadap cabang saat ini (lihat juga `git rebase --onto`):

`git cherry-pick {{komit_awal}}~..{{komit_akhir}}`

- Lakukan perubahan berdasarkan kumpulan komit (tak berurut) terhadap cabang saat ini:

`git cherry-pick {{komit1 komit2 ...}}`

- Lakukan perubahan pada direktori kerja saat ini tanpa mencatat komit baru:

`git cherry-pick {{[-n|--no-commit]}} {{komit}}`
