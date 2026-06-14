#այսոն

> Կատարել JSONPath-ը JSON օբյեկտների վրա:.
> Լրացուցիչ տեղեկություններ. <https://github.com/spyzhov/ajson#console-application>:.

- Կարդացեք JSON ֆայլից և գործարկեք նշված JSONPath արտահայտությունը.:

`ajson '{{$..json[?(@.path)]}}' {{path/to/file.json}}`

- Կարդացեք JSON `stdin`-ից և գործարկեք նշված JSONPath արտահայտությունը՝:

`cat {{path/to/file.json}} | ajson '{{$..json[?(@.path)]}}'`

- Կարդացեք JSON URL-ից և գնահատեք նշված JSONPath արտահայտությունը.:

`ajson '{{avg($..price)}}' '{{https://example.com/api/}}'`

- Կարդացեք մի քանի պարզ JSON և հաշվարկեք արժեքը.:

`echo '{{3}}' | ajson '{{2 * pi * $}}'`
