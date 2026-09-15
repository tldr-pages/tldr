# sha256sum

> Hitung hasil persandian hash (checksum) untuk kumpulan berkas menggunakan algoritma SHA256.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Hitung hash atas satu atau beberapa berkas menggunakan algoritma SHA256:

`sha256sum {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Hitung dan simpan daftar hasil hash beserta alamat berkas asal ke dalam suatu berkas manifes:

`sha256sum {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}} > {{jalan/menuju/berkas_manifes.sha256}}`

- Hitung hash atas isi dari `stdin`:

`{{perintah}} | sha256sum`

- Baca suatu berkas manifest serta lakukan verifikasi atas nilai hash dari isi berkas-berkas tersebut:

`sha256sum {{[-c|--check]}} {{jalan/menuju/berkas_manifes.sha256}}`

- Hanya luarkan pesan-pesan galat ketika terjadi kegagalan atas proses verifikasi:

`sha256sum {{[-c|--check]}} --quiet {{jalan/menuju/berkas_manifes.sha256}}`

- Hanya luarkan pesan-pesan galat dan abaikan berkas-berkas yang tak ditemukan:

`sha256sum --ignore-missing {{[-c|--check]}} --quiet {{jalan/menuju/berkas_manifes.sha256}}`

- Periksa keabsahan isi suatu berkas dengan nilai hash SHA256 yang diketahui:

`echo {{nilai_hash_sha256_yang_diketahui}} {{jalan/menuju/berkas}} | sha256sum {{[-c|--check]}}`
