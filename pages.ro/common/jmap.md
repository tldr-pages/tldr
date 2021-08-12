# jmap

> Instrumentul de hartă a memoriei Java.

- Imprimați mapări de obiecte partajate pentru un proces Java (ieșire cum ar fi pmap):

`jmap {{java_pid}}`

- Imprimare informații rezumat heap:

`jmap -heap {{filename.jar}} {{java_pid}}`

- Histograma tipăririi utilizării heap după tip:

`jmap -histo {{java_pid}}`

- Dump conținutul heap într-un fișier binar pentru analiză cu jhat:

`jmap -dump:format=b,file={{filename}} {{java_pid}}`
