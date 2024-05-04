# truss

> Narzędzie do rozwiązywania problemów poprzez śledzenie wywołań systemowych.
> Odpowiednik strace w SunOS.
> Więcej informacji: <https://www.unix.com/man-page/linux/1/truss>.

- Rozpoczęcie śledzenie programu, wykonując go i śledząc wszystkie procesy potomne:

`truss -f {{program}}`

- Rozpoczęcie śledzenia określonego procesu według jego PID:

`truss -p {{pid}}`

- Rozpoczęcie śledzenia programu, wykonując go, pokazując argumenty i zmienne środowiskowe:

`truss -a -e {{program}}`

- Zliczanie czasu, wywołań i błędów dla każdego wywołania systemowego i raportowanie podsumowania po zakończeniu programu:

`truss -c -p {{pid}}`

Śledzenie procesu filtrując dane wyjściowe według wywołania systemowego:

`truss -p {{pid}} -t {{nazwa_wywolania_systemowego}}`
