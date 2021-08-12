# x11vnc

> Un server VNC care va activa VNC pe un server de afișare existent.
> În mod implicit, serverul se va termina automat după ce toți clienții se deconectează de la acesta.

- Lansarea unui server VNC care permite mai multor clienți să se conecteze:

`x11vnc -shared`

- Lansați un server VNC în modul doar vizualizare și care nu se va termina odată ce ultimul client se deconectează:

`x11vnc -forever -viewonly`

- Lansarea unui server VNC pe un anumit ecran și ecran (ambele începând de la indexul zero):

`x11vnc -display :{{display}}.{{screen}}`

- Lansarea unui server VNC pe ecranul implicit al celui de-al treilea ecran:

`x11vnc -display :{{2}}`

- Lansarea unui server VNC pe al doilea ecran al primului ecran:

`x11vnc -display :{{0}}.{{1}}`
