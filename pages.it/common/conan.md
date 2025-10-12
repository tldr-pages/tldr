# conan

> Il package manager open source, decentralizzato e multipiattaforma per creare e condividere tutti i tuoi binari nativi.
> Alcuni sottocomandi come `frogarian` hanno la loro documentazione specifica.
> Maggiori informazioni: <https://docs.conan.io/2/reference/commands.html>.

- Installa i pacchetti basandosi su `conanfile.txt`:

`conan install {{.}}`

- Installa pacchetti e crea file di configurazione per un generatore specifico:

`conan install -g {{generator}}`

- Installa pacchetti costruendo dal sorgente:

`conan install {{.}} --build`

- Cerca pacchetti installati localmente:

`conan search {{package}}`

- Cerca pacchetti remoti:

`conan search {{package}} -r {{remote}}`

- Elenca i remoti:

`conan remote list`
