# snoop

> Sniffer pakietów sieciowych.
> Odpowiednik tcpdump w systemie SunOS.
> Więcej informacji: <https://www.unix.com/man-page/sunos/1m/snoop>.

- Przechwytywanie pakietów na określonym interfejsie sieciowym:

`snoop -d {{e1000g0}}`

- Zapisywanie przechwyconych pakietów w pliku zamiast ich wyświetlania:

`snoop -o {{sciezka/do/pliku}}`

- Wyświetla szczegółowe podsumowanie warstwy protokołu pakietów z pliku:

`snoop -V -i {{sciezka/do/pliku}}`

- Przechwytuje pakiety sieciowe, które pochodzą z nazwy hosta i trafiają na dany port:

`snoop to port {{port}} from host {{nazwahosta}}`

- Przechwytywanie i wyświetlanie zrzutu heksadecymalnego pakietów sieciowych wymienianych między dwoma adresami IP:

`snoop -x0 -p4 {{ip1}} {{ip2}}`
