# gcrane gc

> Toon images die niet getagged zijn.
> Zal berekenen welke images opgeruimd kunnen worden met garbage-collection.
> Dit kan uitgevoerd worden met `gcrane delete` om ze daadwerkelijk op te ruimen.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Toon niet getagde images:

`gcrane gc {{repository}}`

- Recursief door de repositories heen:

`gcrane gc {{repository}} {{[-r|--recursive]}}`

- Toon de help:

`gcrane gc {{[-h|--help]}}`
