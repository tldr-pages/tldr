# badblocks

> Cari blok-blok memori yang bermasalah dalam suatu piranti penyimpanan.
> Penggunaan beberapa fungsi dalam badblocks dapat mengakibatkan perubahan destruktif, seperti menghapus seluruh data dalam suatu piranti penyimnpanan, termasuk tabel konfigurasi partisi.
> Informasi lebih lanjut: <https://manned.org/badblocks>.

- Lakukan inspeksi terhadap suatu piranti penyimpanan menggunakan mode uji hanya-baca (read-only) yang non-destruktif:

`sudo badblocks {{/dev/sdX}}`

- Lakukan inspeksi terhadap suatu piranti yang tidak dimuat menggunakan mode uji baca-tulis yang [n]on-destruktif:

`sudo badblocks -n {{/dev/sdX}}`

- Lakukan inspeksi terhadap suatu piranti yang tidak dimuat menggunakan mode uji baca ([w]rite) secara destruktif:

`sudo badblocks -w {{/dev/sdX}}`

- Gunakan mode uji baca ([w]rite) destruktif dan tampilkan kemajuan proses secara bertele-tele:

`sudo badblocks -svw {{/dev/sdX}}`

- Dalam mode destruktif, simpan luaran ([o]utput) ke dalam suatu berkas:

`sudo badblocks -o {{jalan/menuju/berkas}} -w {{/dev/sdX}}`

- Gunakan mode destruktif dalam kecepatan yang lebih baik menggunakan ukuran [b]lok sebesar 4K dan jumlah blok ([c]ount) sebesar 64K:

`sudo badblocks -w -b {{4096}} -c {{65536}} {{/dev/sdX}}`
