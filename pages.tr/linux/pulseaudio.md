# pulseaudio

> Ses sistem arkaplan uygulaması ve yöneticisi.
> Daha fazla bilgi: <https://www.freedesktop.org/wiki/Software/PulseAudio/>.

- Pulseaudio'nun çalışıp çalışmadığını kontrol et (sıfır olmayan çıktı, çalışmadığı anlamına gelir):

`pulseaudio --check`

- Pulseaudio'yu arkaplanda çalıştır:

`pulseaudio --start`

- Arkaplanda çalışan tüm pulseaudio uygulamalarını öldür:

`pulseaudio --kill`

- Müsait modülleri sırala:

`pulseaudio --dump-modules`

- Belirtilen argümanlarla bir modülü mevcut çalışan arkaplan uygulamasına yükle:

`pulseaudio --load="{{modül_ismi}} {{argümanlar}}"`
