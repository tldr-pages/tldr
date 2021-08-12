# nologin

> Shell alternativă care împiedică un utilizator să se coneceze.

- Setați carcasa de conectare a unui utilizator la `nologin` pentru a împiedica utilizatorul să se conecteze:

`chsh -s {{user}} nologin`

- Personalizarea mesajului pentru utilizatori cu shell-ul de logare al `nologin`:

`echo "{{declined_login_message}}" > /etc/nologin.txt`
