# pkg-config

> Furnizați detaliile bibliotecilor instalate pentru compilarea aplicațiilor.
> Mai multe informaţii: <https://www.freedesktop.org/wiki/Software/pkg-config/>

- Obțineți lista bibliotecilor și dependențele acestora:

`pkg-config --libs {{library1 library2 ...}}`

- Obțineți lista bibliotecilor, dependențele lor și cflag-urile corespunzătoare pentru gcc:

`pkg-config --cflags --libs {{library1 library2 ...}}`

- Compilați codul cu libgtk-3, libwebkit2gtk-4.0 și toate dependențele lor:

`c++ example.cpp $(pkg-config --cflags --libs gtk+-3.0 webkit2gtk-4.0) -o example`
