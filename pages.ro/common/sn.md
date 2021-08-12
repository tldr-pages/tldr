# sn

> Mono StrongName utilitar pentru semnarea și verificarea ansamblurilor IL.

- Generați o nouă cheie StronGNaming:

`sn -k {{path/to/key.snk}}`

- Re-semneze un ansamblu cu cheia privată specificată:

`sn -R {{path/to/assembly.dll}} {{path/to/key_pair.snk}}`

- Afișați cheia publică a cheii private care a fost utilizată pentru a semna un ansamblu:

`sn -T {{path/to/assembly.exe}}`

- Extrageţi cheia publică într-un fişier:

`sn -e {{path/to/assembly.dll}} {{path/to/output.pub}}`
