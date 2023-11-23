# nm

> Toon symbool namen in object bestanden.
> Meer informatie: <https://manned.org/nm>.

- Toon globale (externe) functies in een bestand (voorafgegaan door T):

`nm -g {{pad/naar/bestand.o}}`

- Toon alleen ongedefinieerde symbolen in een bestand:

`nm -u {{pad/naar/bestand.o}}`

- Toon alle symbolen, ook debugging symbolen:

`nm -a {{pad/naar/bestand.o}}`

- Transformeer C++ symbolen (maak ze leesbaar):

`nm --demangle {{pad/naar/bestand.o}}`
