# enum4linux

> Instrument pentru enumerarea informațiilor Windows și Samba din sistemele de la distanță.
> Acesta încearcă să ofere funcționalități similare cu enum.exe disponibile anterior de la www.bindview.com.
> Mai multe informaţii: <https://labs.portcullis.co.uk/tools/enum4linux/>

- Încercați să enumerați folosind toate metodele:

`enum4linux -a {{remote_host}}`

- Enumerați folosind datele de autentificare date:

`enum4liux -u {{user_name}} -p {{password}} {{remote_host}}`

- Lista numelor de utilizator de la o anumită gazdă:

`enum4liux -U {{remote_host}}`

- Lista de acțiuni:

`enum4liux -S {{remote_host}}`

- Obțineți informații despre OS:

`enum4liux -o {{remote_host}}`
