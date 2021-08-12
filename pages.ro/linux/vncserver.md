# vncserver

> Lansează un desktop VNC (Virtual Network Computing).

- Lansați un server VNC pe următorul afișaj disponibil:

`vncserver`

- Lansarea unui server VNC cu geometrie specifică a ecranului:

`vncserver --geometry {{width}}x{{height}}`

- Omoară o instanță a serverului VNC care rulează pe un anumit afișaj:

`vncserver --kill :{{display_number}}`
