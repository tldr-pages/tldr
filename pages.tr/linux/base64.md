# base64

> base64 veya standart girdi ile kodla veya çöz.
> Daha fazla bilgi için: <https://manned.org/base64>

- Temel kullanım formatı:

`base64 {{seçenek}} {{dosya}}`

- Kodlama yapma (dosya ile):

`base64 {{dosya}}`

- Kodlama yapma (standart girdi ile):

`base64`

`{{standart_girdi}}`(girdinizi yazın)

Ardından <kbd>Ctrl + D </kbd>'yi tuşlayın.

- Çözme (dosya ile):

`base64 {{[-d|--decode]}} {{dosya}}`

- Çözme (standart girdi ile):

`base64 {{[-d|--decode]}}`

`{{standart_girdi}}`(girdinizi yazın)

Ardından <kbd>Ctrl + D </kbd>'yi tuşlayın.

- Kod çözerken Abece dşı karakterleri yok say:

`base64 {{[-d|--decode]}} {{[-i|--ignore-garbage]}}`
