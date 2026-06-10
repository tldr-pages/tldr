# python -m json.tool

> Վավերացրեք և գեղեցիկ տպեք JSON տվյալները:.
> Python-ի ստանդարտ գրադարանի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://docs.python.org/library/json.html#module-json.tool>:.

- Գեղեցիկ տպել JSON ֆայլից.:

`python -m json.tool {{path/to/file.json}}`

- Վավերացրեք և գեղեցիկ տպեք JSON `stdin`-ից:

`echo '{{{"key": "value"}}}' | python -m json.tool`
