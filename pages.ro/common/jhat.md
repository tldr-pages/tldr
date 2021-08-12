# jhat

> Instrument de analiză Java Heap.
> Mai multe informaţii: <https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jhat.html>

- Analizați o dump heap (de la jmap), vizualizați prin http pe portul 7000:

`jhat {{dump_file.bin}}`

- Analizați o imagine heap, specificând un port alternativ pentru serverul http:

`jhat -p {{port}} {{dump_file.bin}}`

- Analizați o groapa de gunoi permițând jhat utiliza până la 8GB RAM (2-4x dimensiunea dump recomandat):

`jhat -J-mx8G {{dump_file.bin}}`
