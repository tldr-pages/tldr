# rsync

> Transfer file ke atau dari sebuah _remote host_ (bukan di antara 2 _remote host_).
> Bisa transfer satuan file, maupun beberapa file yang sesuai dengan pola tertentu.
> Informasi lebih lanjut: <https://download.samba.org/pub/rsync/rsync.1>.

- Transfer file dari lokal ke _remote host_:

`rsync {{lokasi/ke/file_lokal}} {{remote_host}}:{{lokasi/ke/remote_directory}}`

- Transfer file dari _remote host_ ke lokal:

`rsync {{remote_host}}:{{lokasi/ke/remote_file}} {{lokasi/ke/direktori_lokal}}`

- Transfer file dalam mode [a]rsip (untuk menyimpan atribut-atribut) dan terkompres (_[z]ipped_) secara _[v]erbose_ dan progresnya dapat dibaca orang (_[h]uman-readable [P]rogress_):

`rsync {{-zvhP|--compress --verbose --human-readable --partial --progress}} {{lokasi/ke/file_lokal}} {{remote_host}}:{{lokasi/ke/remote_directory}}`

- Transfer direktori dan semua isiny dari remote ke lokal:

`rsync {{-r|--recursive}} {{remote_host}}:{{lokasi/ke/remote_directory}} {{lokasi/ke/direktori_lokal}}`

- Transfer isi direktori (namun bukan direktori itu sendiri) dari remote ke lokal:

`rsync {{-r|--recursive}} {{remote_host}}:{{lokasi/ke/remote_directory}}/ {{lokasi/ke/direktori_lokal}}`

- Transfer direktori secara [r]ecursif, dalam [a]rsip (untuk menyimpan atribut-atribut), menyelesaikan _soft[l]inks_ yang terkandung di sana, dan mengabaikan file-file yang sudah ditransfer kecuali jika file itu lebih baru (_[u]nless newer_):

`rsync {{-auL|--archive --update --copy-links}} {{remote_host}}:{{lokasi/ke/remote_file}} {{lokasi/ke/direktori_lokal}}`

- Transfer file melalui SSH dan hapus file-file lokal yang tidak ada di _remote host_:

`rsync {{-e|--rsh}} ssh --delete {{remote_host}}:{{lokasi/ke/remote_file}} {{lokasi/ke/file_lokal}}`

- Transfer file melalui SSH dengan menggunakan port yang yang berbeda dari bawaan dan tampilkan progres global:

`rsync {{-e|--rsh}} 'ssh -p {{port}}' --info=progress2 {{remote_host}}:{{lokasi/ke/remote_file}} {{lokasi/ke/file_lokal}}`
