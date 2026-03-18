# conda notices

> Recupera le notifiche più recenti dei canali.  
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/latest/commands/notices.html>.

- Mostra le notifiche per il canale predefinito e tutti i canali specificati in `.condarc`:

`conda notices`

- Includi un canale specifico:

`conda notices {{[-c|--channel]}} {{nome_canale}}`

- Ignora i canali predefiniti e quelli definiti in `.condarc`:

`conda notices {{[-c|--channel]}} {{nome_canale}} --override-channels`
