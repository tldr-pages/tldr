# zola

> Un generator de site static într-un singur binar cu totul încorporat.
> Mai multe informaţii: <https://www.getzola.org/documentation/getting-started/cli-usage/>

- Creați structura directorului utilizată de Zola în directorul dat:

`zola init {{my_site}}`

- Construiți întregul site în directorul `public” după ștergerea acestuia:

`zola build`

- Construiți întregul site într-un director diferit:

`zola build --output-dir {{path/to/output_directory/}}`

- Construiți și serviți site-ul folosind un server local (implicit este `127.0.0. 1:1111 `):

`zola serve`

- Construiți toate paginile la fel cum ar fi comanda de compilare, dar fără a scrie oricare dintre rezultatele pe disc:

`zola check`
