# input

> Kirim sinyal input terhadap sebuah perangkat Android.
> Perintah ini hanya dapat dijalankan melalui `adb shell`.
> Informasi lebih lanjut: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Masukkan input karakter (layaknya pada papan kunci / keyboard) terhadap perangkat Android:

`input keyevent {{kode_event}}`

- Masukkan input teks ke dalam perangkat Android (spasi ditandai dengan `%s`):

`input text "{{teks}}"`

- Masukkan input sentuhan layar pada posisi tertentu:

`input tap {{posisi_x}} {{posisi_y}}`

- Simulasikan gerakan usap/swipe terhadap perangkat Android:

`input swipe {{posisi_awal_x}} {{posisi_awal_y}} {{posisi_akhir_x}} {{posisi_akhir_y}} {{durasi_dalam_milidetik}}`

- Simulasikan interaksi tekan-dan-tahan terhadap perangkat Android:

`input swipe {{posisi_x}} {{posisi_y}} {{posisi_x}} {{posisi_y}} {{durasi_dalam_milidetik}}`
