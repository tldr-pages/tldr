# wget

> Descărcați fișiere de pe Web.
> Suportă HTTP, HTTPS și FTP.
> Mai multe informaţii: <https://www.gnu.org/software/wget>

- Descărcați conținutul unui URL într-un fișier (denumit „foo” în acest caz):

`wget {{https://example.com/foo}}`

- Descărcați conținutul unui URL într-un fișier (denumit „bar” în acest caz):

`wget --output-document {{bar}} {{https://example.com/foo}}`

- Descărcați o singură pagină web și toate resursele sale cu intervale de 3 secunde între cereri (scripturi, foi de stil, imagini etc.):

`wget --page-requisites --convert-links --wait=3 {{https://example.com/somepage.html}}`

- Descărcați toate fișierele listate într-un director și subdirectoarele sale (nu descarcă elemente de pagină încorporate):

`wget --mirror --no-parent {{https://example.com/somepath/}}`

- Limitați viteza de descărcare și numărul de reîncercări de conectare:

`wget --limit-rate={{300k}} --tries={{100}} {{https://example.com/somepath/}}`

- Descărcați un fișier de pe un server HTTP utilizând Basic Auth (funcționează și pentru FTP):

`wget --user={{username}} --password={{password}} {{https://example.com}}`

- Continuă o descărcare incompletă:

`wget --continue {{https://example.com}}`

- Descărcați toate adresele URL stocate într-un fișier text într-un anumit director:

`wget --directory-prefix {{path/to/directory}} --input-file {{URLs.txt}}`
