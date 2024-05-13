# snoop

> Sniffer pakietów sieciowych.
> Odpowiednik tcpdump w systemie SunOS.
> Więcej informacji: <https://www.unix.com/man-page/sunos/1m/snoop>.

- Przechwyć pakiety na określonym interfejsie sieciowym:

`snoop -d {{e1000g0}}`

- Zapisz przechwycone pakiety w pliku zamiast ich wyświetlania:

`snoop -o {{ścieżka/do/pliku}}`

- Wyświetl szczegółowe podsumowanie warstwy protokołu pakietów z pliku:

`snoop -V -i {{ścieżka/do/pliku}}`

- Przechwyć pakiety sieciowe, które pochodzą z nazwy hosta i trafiają na dany port:

`snoop to port {{port}} from host {{nazwa_hosta}}`

- Przechwyć i wyświetl zrzut heksadecymalny pakietów sieciowych wymienianych między dwoma adresami IP:

`snoop -x0 -p4 {{ip1}} {{ip2}}`
