# espeak

> Az alapértelmezett hangeszközön keresztül szövegről beszédre történő beszédet használ. További információ: <http://espeak.sourceforge.net>.

- Egy mondat hangos kimondása:

`espeak "I like to ride my bike."`

- Egy fájl hangos kimondása:

`espeak -f {{path/to/file}}`

- A kimenet mentése WAV hangfájlba, ahelyett, hogy közvetlenül beszélne:

`espeak -w {{filename.wav}} "It's GNU plus Linux"`

- Másik hang használata:

`espeak -v {{voice}}`
