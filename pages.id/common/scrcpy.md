# scrcpy

> Tampilkan layar and kontrol perangkat Android anda di dalam desktop.
> Informasi lebih lanjut: <https://github.com/Genymobile/scrcpy>.

- Tampilkan layar sebuah perangkat yang terhubung:

`scrcpy`

- Tampilkan layar perangkat tertentu berdasarkan ID atau alamat IP-nya (temukan menggunakan perintah `adb devices`):

`scrcpy --serial {{0123456789abcdef|192.168.0.1:5555}}`

- Tampilkan layar dalam mode layar penuh / fullscreen:

`scrcpy --fullscreen`

- Putarkan tampilan layar perangkat dalam kelipatan 90 derajat (berlawanan arah jarum jam):

`scrcpy --rotation {{0|1|2|3}}`

- Tunjukkan indikator sentuhan pada perangkat fisik:

`scrcpy --show-touches`

- Rekam tampilan layar perangkat ke dalam file video tertentu:

`scrcpy --record {{jalan/menuju/file.mp4}}`

- Tentukan direktori yang akan digunakan untuk memindahkan file (non-APK) ke dalam perangkat melalui drag-and-drop:

`scrcpy --push-target {{jalan/menuju/direktori}}`
