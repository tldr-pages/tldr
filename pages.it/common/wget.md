# wget

> Scarica file dal Web.
> Supporta HTTP, HTTPS, FTP.
> Vedi anche: `wcurl`, `curl`.
> Maggiori informazioni: <https://www.gnu.org/software/wget/manual/wget.html>.

- Scarica il contenuto dell'URL in un file (dal nome "abcd" in questo caso):

`wget {{https://example.com/abcd}}`

- Scarica il contenuto dell'URL in un file (dal nome "efgh" in questo caso):

`wget {{[-O|--output-document]}} {{efgh}} {{https://example.com/abcd}}`

- Scarica una singola pagina web e tutte le sue risorse (script, immagini, stili, ecc..) aspettando 3 secondi dopo ogni richiesta:

`wget {{[-pkw|--page-requisites --convert-links --wait]}} 3 {{https://example.com/pagina_web.html}}`

- Scarica tutti i file elencati nella directory e nelle sue sotto-directory (non scarica gli elementi incorporati nella pagina):

`wget {{[-mnp|--mirror --no-parent]}} {{https://example.com/unqualchepercorso/}}`

- Limita la velocità di download e il numero di tentativi di connessione:

`wget --limit-rate {{300k}} {{[-t|--tries]}} {{100}} {{https://example.com/unqualchepercorso/}}`

- Scarica un file da un server HTTP trasmettendo le credenziali tramite Basis Auth (funzione anche con FTP):

`wget --user {{nome_utente}} --password {{password}} {{https://example.com}}`

- Riprende un download incompleto:

`wget {{[-c|--continue]}} {{https://example.com}}`

- Scarica tutti gli URL contenuti in un file di testo in una directory specificata:

`wget {{[-P|--directory-prefix]}} {{percorso/della/directory}} {{[-i|--input-file]}} {{lista_di_url.txt}}`
