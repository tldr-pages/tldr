# git diff

> Tampilkan perubahan yang terjadi pada berkas-berkas yang diawasi.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-diff>.

- Tampilkan perubahan yang belum dimasukkan ke dalam stage:

`git diff`

- Tampilkan perubahan seluruh berkas (termasuk perubahan yang dimasukkan ke dalam stage):

`git diff HEAD`

- Hanya tampilkan perubahan yang dimasukkan ke dalam stage (dipertimbangkan, namun belum disahkan dalam suatu komit):

`git diff --staged`

- Tampilkan perubahan-perubahan dari seluruh komit sejak suatu hari/tanggal (baik dalam ekspresi tanggal bahasa Inggris seperti "1 week 2 days", maupun format tanggal ISO):

`git diff 'HEAD@{{{3 months|weeks|days|hours|seconds ago}}}'`

- Tampilkan statistik atas perubahan-perubahan yang dilakukan, seperti daftar berkas yang diubah, histogram, dan total jumlah penambahan/pengurangan baris teks dalam berkas:

`git diff --stat {{komit}}`

- Tampilkan laporan ringkasan atas pembuatan, penamaan ulang, dan perubahan mode terhadap berkas-berkas sejak komit yang ditentukan:

`git diff --summary {{komit}}`

- Bandingkan suatu berkas antara dua cabang (branch) atau komit:

`git diff {{cabang_1}}..{{cabang_2}} {{jalan/menuju/berkas}}`

- Bandingkan beberapa berkas dari cabang saat ini dengan cabang lainnya:

`git diff {{cabang_lainnya}}:{{jalan/menuju/berkas2}} {{jalan/menuju/berkas1}}`
