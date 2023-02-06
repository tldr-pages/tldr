# mail

> A parancs a felhasználó postafiókján dolgozik, ha nincs argumentum megadva.
> E-mail küldéséhez az üzenet szövegét a standard bemenetről kell felépíteni.
> További információ: <https://manned.org/mail>.

- Gépelt e-mail üzenet küldése. Az alábbi parancssor az Enter billentyű lenyomása után folytatódik. CC email-id bevitele (opcionális) Majd Enter. Üzenet szövegének bevitele (többsoros akár). Befejezéséhez nyomja meg a Ctrl-D billentyűt:

`mail --subject="{{subject line}}" {{to_user@example.com}}`

- Fájltartalmat tartalmazó e-mail küldése:

`mail --subject="{{$HOSTNAME filename.txt}}" {{to_user@example.com}} < {{path/to/filename.txt}}`

- Küldjön egy `tar.gz` fájlt mellékletként:

`tar cvzf - {{path/to/directory1 path/to/directory2}} | uuencode {{data.tar.gz}} | mail --subject="{{subject_line}}" {{to_user@example.com}}`
