# espeak

> Utilizează textul transformat în vorbire pentru a vorbi prin dispozitivul de sunet implicit.
> Mai multe informaţii: <http://espeak.sourceforge.net>

- Vorbeşte o frază cu voce tare:

`espeak "I like to ride my bike."`

- Vorbește un fișier cu voce tare:

`espeak -f {{filename}}`

- Salvați ieșirea într-un fișier audio WAV, mai degrabă decât să o vorbiți direct:

`espeak -w {{filename.wav}} "It's GNU plus Linux"`

- Foloseşte o altă voce:

`espeak -v {{voice}}`
