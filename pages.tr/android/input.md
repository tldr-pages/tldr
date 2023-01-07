# input

> Olay kodlarını ve dokunmatik ekran mimiklerini bir Android cihazına yolla.
> Bu komut yalnızca `adb shell` ile kullanılabilir.
> Daha fazla bilgi için: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Bir Android cihazına tek karakter için etkinlik kodu gönder:

`input keyevent {{etkinlik_kodu}}`

- Bir Android cihazına yazı gönder (`%s` boşlukları temsil eder):

`input text "{{yazı}}"`

- Bir Android cihazına tek dokunuş gönder:

`input tap {{x_poz}} {{y_poz}}`

- Bir Android cihazına kaydırma mimiği gönder:

`input swipe {{x_başlangıç}} {{y_başlangıç}} {{x_son}} {{y_son}} {{ms_süre}}`

- Bir Android cihazına kaydırma mimiği kullanarak uzun dokunuş gönder:

`input swipe {{x_poz}} {{y_poz}} {{x_poz}} {{y_poz}} {{ms_süre}}`
