# git check-ref-format

> Cek apakah nama suatu referensi (refname) sesuai syarat, dan keluar dengan nilai status di luar angka nol jika tidak.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-check-ref-format>.

- Cek kesesuaian format suatu nama referensi:

`git check-ref-format {{refs/head/refname}}`

- Cetak nama cabang yang terakhir kali diperiksa sebelum mengganti ke cabang saat ini:

`git check-ref-format --branch @{-1}`

- Lakukan normalisasi terhadap nama referensi:

`git check-ref-format --normalize {{refs/head/refname}}`
