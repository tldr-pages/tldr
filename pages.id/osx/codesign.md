# codesign

> Buat dan manipulasi tanda tangan digital atas kode program untuk macOS.
> Informasi lebih lanjut: <https://keith.github.io/xcode-man-pages/codesign.1.html>.

- Tandatangani suatu aplikasi dengan suatu sertifikat:

`codesign --sign "{{Nama Perusahaan Saya}}" {{jalan/menuju/berkas_aplikasi.app}}`

- Lakukan verifikasi atas sertifikat dalam suatu aplikasi:

`codesign --verify {{jalan/menuju/berkas_aplikasi.app}}`
