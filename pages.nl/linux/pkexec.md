# pkexec

> Voer commando's uit als een andere gebruiker.
> Vraagt om een wachtwoord via een GUI indien beschikbaar.
> Zie ook: `sudo`, `run0`, `doas`.
> Meer informatie: <https://polkit.pages.freedesktop.org/polkit/pkexec.1.html>.

- Voer een commando uit als root:

`pkexec {{commando}}`

- Wissel van gebruiker naar root:

`pkexec`

- Voer een commando uit als een specifieke gebruiker:

`pkexec --user {{gebruikersnaam}} {{commando}}`
