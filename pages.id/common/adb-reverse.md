# adb reverse

> Android Debug Bridge Reverse: membalik koneksi socket dari emulator Android atau perangkat Android terhubung.
> Informasi lebih lanjut: <https://developer.android.com/studio/command-line/adb>.

- Daftar semua koneksi socket terbalik dari emulator dan perangkat:

`adb reverse --list`

- Membalik port TCP dari emulator/perangkat ke localhost:

`adb reverse tcp:{{port_jarak_jauh}} tcp:{{port_lokal}}`

- Melepas koneksi socket terbalik dari emulator/perangkat:

`adb reverse --remove tcp:{{port_jarak_jauh}}`

- Melepas semua koneksi socket terbalik dari semua emulator dan perangkat:

`adb reverse --remove-all`
