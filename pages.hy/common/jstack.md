# jstack

> Java stack հետագծման գործիք:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/jstack>:.

- Java պրոցեսի բոլոր թելերի համար տպեք Java stack հետքերը.:

`jstack {{java_pid}}`

- Տպել խառը ռեժիմով (Java/C++) կույտի հետքեր Java գործընթացի բոլոր թելերի համար.:

`jstack -m {{java_pid}}`

- Տպեք կույտերի հետքերը Java հիմնական աղբավայրից.:

`jstack {{/usr/bin/java}} {{file.core}}`
