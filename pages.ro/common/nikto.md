# nikto

> Web server scaner care efectuează teste împotriva serverelor web pentru mai multe elemente.
> Mai multe informaţii: <https://cirt.net/Nikto2>

- Efectuați o scanare Nikto de bază împotriva unei gazde țintă:

`perl nikto.pl -h {{192.168.0.1}}`

- Specificați numărul portului atunci când efectuați o scanare de bază:

`perl nikto.pl -h {{192.168.0.1}} -p {{443}}`

- Scanarea porturilor și protocoalelor cu sintaxă URL completă:

`perl nikto.pl -h {{https://192.168.0.1:443/}}`

- Scanarea mai multor porturi în aceeași sesiune de scanare:

`perl nikto.pl -h {{192.168.0.1}} -p {{80,88,443}}`

- Actualizare la cele mai recente plugin-uri și baze de date:

`perl nikto.pl -update`
