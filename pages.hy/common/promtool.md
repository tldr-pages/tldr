# promtool

> Գործիքներ Պրոմեթևսի մոնիտորինգի համակարգի համար:.
> Լրացուցիչ տեղեկություններ. <https://prometheus.io/docs/prometheus/latest/getting_started/>:.

- Ստուգեք՝ արդյոք կազմաձևման ֆայլերը վավեր են, թե ոչ (եթե առկա են հաշվետվության սխալներ).:

`promtool check config {{config_file.yml}}`

- Ստուգեք՝ արդյոք կանոնների ֆայլերը վավեր են, թե ոչ (եթե առկա են հաշվետվության սխալներ).:

`promtool check rules {{rules_file.yml}}`

- Անցեք Պրոմեթևսի չափումները `stdin`-ից՝ ստուգելու դրանց հետևողականությունն ու ճիշտությունը.:

`curl --silent {{http://example.com:9090/metrics/}} | promtool check metrics`

- Միավորի թեստեր կանոնների կազմաձևման համար.:

`promtool test rules {{test_file.yml}}`
