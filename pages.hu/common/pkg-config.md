# pkg-config

> A telepített könyvtárak adatainak megadása az alkalmazások fordításához. További információ: <https://www.freedesktop.org/wiki/Software/pkg-config/>.

- A könyvtárak és függőségeik listájának lekérdezése:

`pkg-config --libs {{library1 library2 ...}}`

- A könyvtárak listájának, függőségeinek és a megfelelő cflag-eknek a lekérése a gcc számára:

`pkg-config --cflags --libs {{library1 library2 ...}}`

- Fordítsa le a kódot libgtk-3, libwebkit2gtk-4.0 és összes függőségükkel:

`c++ example.cpp $(pkg-config --cflags --libs gtk+-3.0 webkit2gtk-4.0) -o example`
