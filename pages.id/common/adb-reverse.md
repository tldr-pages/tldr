# adb reverse

> Android Debug Bridge Reverse: membalik koneksi socket dari emulator Android atau perangkat Android terhubung.
> Informasi lebih lanjut: <https://developer.android.com/studio/command-line/adb>.

- Daftar semua koneksi socket terbalik dari emulator dan perangkat:

`adb reverse --list`

- Membalik port TCP dari emulator/perangkat ke localhost:

`adb reverse tcp:{{remote_port}} tcp:{{local_port}}`

- Melepas koneksi socket terbalik dari emulator/perangkat:

`adb reverse --remove tcp:{{remote_port}}`

- Melepas semua koneksi socket terbalik dari semua emulator dan perangkat:

`adb reverse --remove-all`
