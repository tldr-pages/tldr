# trap

> Executați automat comenzi după primirea semnalelor prin procese sau prin sistemul de operare.
> Poate fi folosit pentru a efectua curățări pentru întreruperi de către utilizator sau alte acțiuni.
> Mai multe informaţii: <https://manned.org/trap>

- Lista semnalelor disponibile pentru setarea capcanelor pentru:

`trap -l`

- Lista capcanelor active pentru carcasa curentă:

`trap -p`

- Setați o capcană pentru a executa comenzi atunci când unul sau mai multe semnale sunt detectate:

`trap 'echo "Caught signal {{SIGHUP}}"' {{SIGHUP}}`

- Îndepărtați capcanele active:

`trap - {{SIGHUP}} {{SIGINT}}`
