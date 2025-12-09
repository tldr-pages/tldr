# cal

> Wyświetl kalendarz.
> Więcej informacji: <https://man.netbsd.org/cal.1>.

- Wyświetl kalendarz na bieżący miesiąc:

`cal`

- Wyświetl kalendarz na określony rok:

`cal {{rok}}`

- Wyświetl kalendarz dla określonego miesiąca i roku:

`cal {{miesiąc}} {{rok}}`

- Wyświetl cały kalendarz na bieżący rok z użyciem dni [j]uliańskich (dni liczone od 1, począwszy od 1 stycznia):

`cal -y -j`

- Wyróżnij (z ang. [h]ighlight) dzisiejszą datę i wyświetl [3] miesiące ją obejmujące:

`cal -h -3 {{miesiąc}} {{rok}}`

- Wyświetl 2 miesiące przed (z ang. [B]efore) i 3 po (z ang. [A]fter) określonym [m]iesiącu bieżącego roku:

`cal -A 3 -B 2 {{miesiąc}}`

- Wyświetl określoną liczbę miesięcy przed i po ([C]ontext) określonym miesiącu:

`cal -C {{miesiące}} {{miesiąc}}`

- Określ początkowy [d]zień tygodnia (0: niedziela, 1: poniedziałek, ..., 6: sobota):

`cal -d {{0..6}}`
