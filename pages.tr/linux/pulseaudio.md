# pulseaudio

> Ses sistem arkaplan uygulaması ve yöneticisi.
> Daha fazla bilgi için: <https://manned.org/pulseaudio>.

- Pulseaudio'nun çalışıp çalışmadığını kontrol et (sıfır olmayan çıktı, çalışmadığı anlamına gelir):

`pulseaudio --check`

- Pulseaudio'yu arkaplanda çalıştır:

`pulseaudio --start`

- Arkaplanda çalışan tüm PulseAudio uygulamalarını öldür:

`pulseaudio {{[-k|--kill]}}`

- Müsait modülleri sırala:

`pulseaudio --dump-modules`

- Belirtilen argümanlarla bir modülü mevcut çalışan arkaplan uygulamasına yükle:

`pulseaudio {{[-L|--load]}} "{{modül_ismi}} {{argümanlar}}"`
