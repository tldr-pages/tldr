# surfraw

> CLI pentru a interoga o varietate de motoare de căutare pe web.
> Constă dintr-o colecție de elvi, fiecare dintre care știe cum să caute un anumit site.
> Mai multe informaţii: <http://surfraw.org>

- Afișează lista scripturilor de căutare a site-urilor web acceptate (elvi):

`surfraw -elvi`

- Deschideți pagina de rezultate a elvi pentru o anumită căutare în browser:

`surfraw {{elvi}} "{{search_terms}}"`

- Afișați o descriere elvi și opțiunile sale specifice:

`surfraw {{elvi}} -local-help`

- Căutați folosind un elvi cu opțiuni specifice și deschideți pagina cu rezultate în browser:

`surfraw {{elvi}} {{elvi_options}} "{{search_terms}}"`

- Afișați adresa URL la pagina de rezultate a elvi pentru o anumită căutare:

`surfraw -print {{elvi}} "{{search_terms}}"`

- Caută folosind aliasul:

`sr {{elvi}} "{{search_terms}}"`
