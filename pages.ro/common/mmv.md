# mmv

> Mutarea și redenumirea fișierelor în bloc.

- Redenumiți toate fișierele cu o anumită extensie într-o altă extensie:

`mmv "*{{.old_extension}}" "#1{{.new_extension}}"`

- Copie `raport6part4.txt` la `. /french/rapport6partie4.txt `împreună cu toate fișierele denumite în mod similar:

`mmv -c "{{report*part*.txt}}" "{{./french/rapport#1partie#2.txt}}"`

- Adăugați toate fișierele `.txt` într-un singur fișier:

`mmv -a "{{*.txt}}" "{{all.txt}}"`

- Conversia datelor în numele fişierelor din formatul „M-D-Y” în format „D-M-Y”:

`mmv "{{[0-1][0-9]-[0-3][0-9]-[0-9][0-9][0-9][0-9].txt}}" "{{#3#4-#1#2-#5#6#7#8.txt}}"`
