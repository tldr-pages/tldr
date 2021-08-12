# zenity

> Afișează dialogurile din scripturile de linie de comandă/coajă.
> Returnați valorile inserate de utilizator sau 1 dacă eroare.

- Afișează dialogul de întrebări implicite:

`zenity --question`

- Afișează un dialog de informații care afișează textul „Bună ziua!” :

`zenity --info --text="{{Hello!}}"`

- Afișați un formular de nume/parolă și ieșiți datele separate prin „;”:

`zenity --forms --add-entry="{{Name}}" --add-password="{{Password}}" --separator="{{;}}"`

- Afișează un formular de selecție a fișierelor în care utilizatorul poate selecta numai directoarele:

`zenity --file-selection --directory`

- Afișează o bară de progres care actualizează mesajul său în fiecare secundă și arată un procent de progres:

`{{(echo "#1"; sleep 1; echo "50"; echo "#2"; sleep 1; echo "100")}} | zenity --progress`
