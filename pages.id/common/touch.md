# touch

> Buat berkas-berkas kosong baru dan setel waktu akses dan modifikasi terhadap para berkas.
> Informasi lebih lanjut: <https://manned.org/touch>.

- Buat kumpulan berkas baru:

`touch {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Atur informasi waktu [a]kses atau [m]odifikasi pada kumpulan berkas yang telah tersedia dalam penyimpanan, dan jangan membuat ([c]reate) berkas baru jika tak tersedia dalam penyimpanan:

`touch {{[-c|--no-create]}} -{{a|m}} {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Atur informasi wak[t]u terhadap kumpulan berkas, dan jangan membuat ([c]reate) berkas baru jika tak tersedia dalam penyimpanan:

`touch {{[-c|--no-create]}} -t {{YYYYMMDDHHMM.SS}} {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Gunakan informasi wak[t]u atas suatu berkas referensi terhadap kumpulan berkas yang diolah, dan jangan membuat ([c]reate) berkas baru jika tak tersedia dalam penyimpanan:

`touch {{[-c|--no-create]}} {{[-r|--reference]}} {{jalan/menuju/berkas_referensi}} {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`
