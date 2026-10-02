# b2sum

> Hitung hasil persandian hash (checksum) untuk kumpulan berkas menggunakan algoritma BLAKE2.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/b2sum-invocation.html>.

- Hitung hash atas satu atau beberapa berkas menggunakan algoritma BLAKE2:

`b2sum {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Hitung dan simpan daftar hasil hash beserta alamat berkas asal ke dalam suatu berkas manifes:

`b2sum {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}} > {{jalan/menuju/berkas_manifes.b2}}`

- Hitung hash atas isi dari `stdin`:

`{{perintah}} | b2sum`

- Baca suatu berkas manifest serta lakukan verifikasi atas nilai hash dari isi berkas-berkas tersebut:

`b2sum {{[-c|--check]}} {{jalan/menuju/berkas_manifes.b2}}`

- Hanya luarkan pesan-pesan galat ketika terjadi kegagalan atas proses verifikasi:

`b2sum {{[-c|--check]}} --quiet {{jalan/menuju/berkas_manifes.b2}}`

- Hanya luarkan pesan-pesan galat dan abaikan berkas-berkas yang tak ditemukan:

`b2sum --ignore-missing {{[-c|--check]}} --quiet {{jalan/menuju/berkas_manifes.b2}}`

- Periksa keabsahan isi suatu berkas dengan nilai hash BLAKE2 yang diketahui:

`echo {{nilai_hash_blake2_yang_diketahui}} {{jalan/menuju/berkas}} | b2sum {{[-c|--check]}}`
