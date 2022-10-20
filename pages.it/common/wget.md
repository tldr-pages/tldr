# wget

> Scarica file dal Web.
> Supporta HTTP, HTTPS, FTP.
> Maggiori informazioni: <https://www.gnu.org/software/wget>.

- Scarica il contenuto dell'URL in un file (dal nome "abcd" in questo caso):

`wget {{https://esempio.com/abcd}}`

- Scarica il contenuto dell'URL in un file (dal nome "efgh" in questo caso):

`wget --output-document {{efgh}} {{https://esempio.com/abcd}}`

- Scarica una singola pagina web e tutte le sue risorse (script, immagini, stili, ecc..) aspettando 3 secondi dopo ogni richiesta:

`wget --page-requisites --convert-links --wait=3 {{https://esempio.com/pagina_web.html}}`

- Scarica tutti i file elencati nella directory e nelle sue sotto-directory (non scarica gli elementi incorporati nella pagina):

`wget --mirror --no-parent {{https://esempio.com/unqualchepercorso/}}`

- Limita la velocità di download e il numero di tentativi di connessione:

`wget --limit-rate={{300k}} --tries={{100}} {{https://esempio.com/unqualchepercorso/}}`

- Scarica un file da un server HTTP trasmettendo le credenziali tramite Basis Auth (funzione anche con FTP):

`wget --user={{nome_utente}} --password={{password}} {{https://esempio.com}}`

- Riprende un download incompleto:

`wget --continue {{https://esempio.com}}`

- Scarica tutti gli URL contenuti in un file di testo in una directory specificata:

`wget --directory-prefix {{percorso/della/directory}} --input-file {{lista_di_URL.txt}}`
