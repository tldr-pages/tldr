# pdf առանձին

> Դյուրակիր փաստաթղթի ձևաչափի (PDF) ֆայլի էջի արդյունահանող:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/pdfseparate>:.

- Քաղեք էջերը PDF ֆայլից և յուրաքանչյուր էջի համար պատրաստեք առանձին PDF ֆայլ.:

`pdfseparate {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}`

- Նշեք արդյունահանման առաջին / մեկնարկային էջը.:

`pdfseparate -f {{3}} {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}`

- Նշեք արդյունահանման վերջին էջը.:

`pdfseparate -l {{10}} {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}`
