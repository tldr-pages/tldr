# vncviewer

> Lansează un client VNC (Virtual Network Computing).

- Lansarea unui client VNC care se conectează la o gazdă pe un anumit afișaj:

`vncviewer {{host}}:{{display_number}}`

- Lansarea în modul ecran complet:

`vncviewer -FullScreen {{host}}:{{display_number}}`

- Lansarea unui client VNC cu o geometrie specifică a ecranului:

`vncviewer --geometry {{width}}x{{height}} {{host}}:{{display_number}}`

- Lansarea unui client VNC care se conectează la o gazdă pe un anumit port:

`vncviewer {{host}}::{{port}}`
