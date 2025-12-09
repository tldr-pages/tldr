# ssh

> Secure Shell adalah protokol yang digunakan untuk masuk (log on) secara aman ke sistem jarak jauh.
> Dapat digunakan untuk masuk atau menjalankan perintah pada server jarak jauh.
> Informasi lebih lanjut: <https://man.openbsd.org/ssh>.

- Terhubung ke server jarak jauh:

`ssh {{nama_pengguna}}@{{host_jarak_jauh}}`

- Terhubung ke server jarak jauh dengan identitas (kunci privat) tertentu:

`ssh -i {{lokasi/ke/berkas_kunci}} {{nama_pengguna}}@{{host_jarak_jauh}}`

- Terhubung ke server jarak jauh dengan IP `10.0.0.1` dan menggunakan [p]ort tertentu (Catatan: `10.0.0.1` bisa disingkat menjadi `10.1`):

`ssh {{nama_pengguna}}@10.0.0.1 -p {{2222}}`

- Jalankan perintah di server jarak jauh dengan alokasi [t]ty agar dapat berinteraksi dengan perintah tersebut:

`ssh {{nama_pengguna}}@{{host_jarak_jauh}} -t {{perintah}} {{argumen_perintah}}`

- SSH tunneling: [D]ynamic port forwarding (proksi SOCKS pada `localhost:1080`):

`ssh -D {{1080}} {{nama_pengguna}}@{{host_jarak_jauh}}`

- SSH tunneling: Meneruskan (forward) port tertentu (`localhost:9999` ke `example.org:80`) sekaligus menonaktifkan alokasi pseudo-[T]ty dan eksekusi perintah jarak jauh ([N]):

`ssh -L {{9999}}:{{example.org}}:{{80}} -N -T {{nama_pengguna}}@{{host_jarak_jauh}}`

- SSH [J]umping: Terhubung ke server jarak jauh melalui sebuah jumphost (Beberapa lompatan jump dapat ditentukan, dipisahkan dengan koma):

`ssh -J {{nama_pengguna}}@{{host_jump}} {{nama_pengguna}}@{{host_jarak_jauh}}`

- Tutup sesi yang macet (hang):

`<Enter><~><.>`
