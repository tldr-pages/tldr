# truss

> Narzędzie do rozwiązywania problemów poprzez śledzenie wywołań systemowych.
> Odpowiednik strace w SunOS.
> Więcej informacji: <https://www.unix.com/man-page/linux/1/truss>.

- Rozpocznij śledzenie programu, wykonując go i śledząc wszystkie procesy potomne:

`truss -f {{program}}`

- Rozpocznij śledzenie określonego procesu według jego PID:

`truss -p {{pid}}`

- Rozpocznij śledzenie programu, wykonując go, pokazując argumenty i zmienne środowiskowe:

`truss -a -e {{program}}`

- Zlicz czas, wywołania i błędy dla każdego wywołania systemowego i raportuj podsumowanie po zakończeniu programu:

`truss -c -p {{pid}}`

- Śledź proces filtrując dane wyjściowe według wywołania systemowego:

`truss -p {{pid}} -t {{nazwa_wywolania_systemowego}}`
