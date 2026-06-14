# proxify

> Բազմակողմանի և շարժական պրոքսի` HTTP/HTTPS երթևեկությունը բռնելու, կառավարելու և վերարտադրելու համար:.
> Տես նաև՝ `mitmproxy`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/projectdiscovery/proxify#usage>:.

- Սկսեք HTTP վստահված անձ (loopback ցանցի միջերեսի `127.0.0.1` և `8888` միացքի վրա):

`proxify`

- Սկսեք HTTP վստահված անձը հատուկ ցանցային միջերեսի և միացքի վրա (կարող է պահանջվել `sudo` `1024`-ից ցածր նավահանգստի համարի համար):

`proxify {{[-ha|-http-addr]}} "{{ip_address}}:{{port_number}}"`

- Նշեք ելքային ձևաչափը և ելքային ֆայլը.:

`proxify {{[-of|-output-format]}} {{jsonl|yaml}} {{[-o|-output]}} {{path/to/file}}`

- Ցուցադրել օգնությունը.:

`proxify -h`
