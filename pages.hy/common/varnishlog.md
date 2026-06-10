# լաքապատ

> Ցուցադրել լաքի տեղեկամատյանները:.
> Լրացուցիչ տեղեկություններ. <https://vinyl-cache.org/docs/trunk/reference/varnishlog.html>:.

- Ցուցադրել տեղեկամատյանները իրական ժամանակում.:

`varnishlog`

- Ցուցադրել միայն կոնկրետ տիրույթի հարցումները.:

`varnishlog -q 'ReqHeader eq "Host: {{example.com}}"'`

- Ցուցադրել միայն POST հարցումները.:

`varnishlog -q 'ReqMethod eq "{{POST}}"'`

- Ցուցադրել միայն կոնկրետ ուղու հարցումները.:

`varnishlog -q 'ReqURL eq "/{{path}}"'`

- Ցուցադրել միայն `regex`-ին համապատասխանող ուղիների հարցումները:

`varnishlog -q 'ReqURL ~ "{{regex}}"'`
