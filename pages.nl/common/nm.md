# nm

> Toon symbool namen in object bestanden.
> Meer informatie: <https://manned.org/nm>.

- Toon globale (externe) functies in een bestand (voorafgegaan door T):

`nm {{[-g|--extern-only]}} {{pad/naar/bestand.o}}`

- Toon alleen ongedefinieerde symbolen in een bestand:

`nm {{[-u|--undefined-only]}} {{pad/naar/bestand.o}}`

- Toon alle symbolen, ook debugging symbolen:

`nm {{[-a|--debug-syms]}} {{pad/naar/bestand.o}}`

- Transformeer C++ symbolen (maak ze leesbaar):

`nm {{[-C|--demangle]}} {{pad/naar/bestand.o}}`
