# dos2unix

> Ubah format pengakhiran baris teks pada suatu berkas teks (plaintext) dari format DOS menuju Unix.
> Program ini menggantikan simbol CRLF menjadi LF.
> Lihat juga: `unix2dos`, `unix2mac`, dan `mac2unix`.
> Informasi lebih lanjut: <https://manned.org/dos2unix>.

- Ganti format pengakhiran baris teks dan simpan perubahan pada berkas yang sama:

`dos2unix {{jalan/menuju/berkas}}`

- Ganti format namun simpan perubahan sebagai berkas baru:

`dos2unix {{[-n|--newfile]}} {{jalan/menuju/berkas}} {{jalan/menuju/berkas_baru}}`

- Tampilkan informasi suatu berkas teks:

`dos2unix {{[-i|--info]}} {{jalan/menuju/berkas}}`

- Tetap jaga/tambahkan/hapus simbol Byte Order Mark (BOM) saat mengubah isi berkas:

`dos2unix --{{keep-bom|add-bom|remove-bom}} {{jalan/menuju/berkas}}`
