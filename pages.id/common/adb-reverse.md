# adb reverse

> Android Debug Bridge Reverse: membalik koneksi socket dari perangkat atau emulator Android yang terhubung.
> Informasi lebih lanjut: <https://developer.android.com/tools/adb>.

- Tampilkan daftar semua koneksi socket terbalik dari emulator dan perangkat:

`adb reverse --list`

- Balikkan akses port TCP dari emulator/perangkat menuju localhost:

`adb reverse tcp:{{port_jarak_jauh}} tcp:{{port_lokal}}`

- Balikkan akses port TCP dari emulator/perangkat spesifik (berdasarkan nomor induk / [s]erial perangkat) menuju localhost:

`adb -s {{ID_perangkat}} reverse tcp:{{remote_port}} tcp:{{local_port}}`

``

- Lepaskan koneksi socket terbalik dari emulator/perangkat:

`adb reverse --remove tcp:{{port_jarak_jauh}}`

- Lepaskan semua koneksi socket terbalik dari semua emulator dan perangkat:

`adb reverse --remove-all`
