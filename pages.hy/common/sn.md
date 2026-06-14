# sn

> Mono StrongName կոմունալ IL հավաքների ստորագրման և ստուգման համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/sn>:.

- Ստեղծեք նոր StrongNaming բանալի.:

`sn -k {{path/to/key.snk}}`

- Վերստորագրեք ժողովը նշված մասնավոր բանալիով.:

`sn -R {{path/to/assembly.dll}} {{path/to/key_pair.snk}}`

- Ցույց տալ մասնավոր բանալիի հանրային բանալին, որն օգտագործվել է ժողովը ստորագրելու համար.:

`sn -T {{path/to/assembly.exe}}`

- Արտահանեք ֆայլի հանրային բանալին.:

`sn -e {{path/to/assembly.dll}} {{path/to/output.pub}}`
