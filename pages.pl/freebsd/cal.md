# cal

> Wyświetl kalendarz z wyróżnionym bieżącym dniem.
> Więcej informacji: <https://man.freebsd.org/cgi/man.cgi?cal>.

- Wyświetl kalendarz dla obecnego miesiąca:

`cal`

- Wyświetl kalendarz dla określonego roku:

`cal {{rok}}`

- Wyświetl kalendarz dla określonego miesiąca i roku:

`cal {{miesiąc}} {{rok}}`

- Wyświetl cały kalendarz na bieżący rok (z ang. [y]ear):

`cal -y`

- Nie wyróżniaj (z ang. [h]ighlight) dzisiejszej daty i wyświetl [3] miesiące ją obejmujące:

`cal -h -3 {{miesiąc}} {{rok}}`

- Wyświetl 2 miesiące przed (z ang. [B]efore) i 3 po (z ang. [A]fter) określonym [m]iesiącu bieżącego roku:

`cal -A 3 -B 2 {{miesiąc}}`

- Wyświetl dni [j]uliańskie (zaczynając od jeden, numerowane od 1 stycznia):

`cal -j`
