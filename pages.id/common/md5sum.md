# md5sum

> Hitung hasil persandian hash (checksum) untuk kumpulan berkas menggunakan algoritma MD5.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/md5sum-invocation.html>.

- Hitung hash atas satu atau beberapa berkas menggunakan algoritma MD5:

`md5sum {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Hitung dan simpan daftar hasil hash beserta alamat berkas asal ke dalam suatu berkas manifes:

`md5sum {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}} > {{jalan/menuju/berkas_manifes.md5}}`

- Hitung hash atas isi dari `stdin`:

`{{perintah}} | md5sum`

- Baca suatu berkas manifest serta lakukan verifikasi atas nilai hash dari isi berkas-berkas tersebut:

`md5sum {{[-c|--check]}} {{jalan/menuju/berkas_manifes.md5}}`

- Hanya luarkan pesan-pesan galat ketika terjadi kegagalan atas proses verifikasi:

`md5sum {{[-c|--check]}} --quiet {{jalan/menuju/berkas_manifes.md5}}`

- Hanya luarkan pesan-pesan galat dan abaikan berkas-berkas yang tak ditemukan:

`md5sum --ignore-missing {{[-c|--check]}} --quiet {{jalan/menuju/berkas_manifes.md5}}`

- Periksa keabsahan isi suatu berkas dengan nilai hash MD5 yang diketahui:

`echo {{nilai_hash_md5_yang_diketahui}} {{jalan/menuju/berkas}} | md5sum {{[-c|--check]}}`
