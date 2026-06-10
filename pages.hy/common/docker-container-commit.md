# docker բեռնարկղային պարտավորություն

> Ստեղծեք նոր պատկեր կոնտեյների փոփոխություններից:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/container/commit/>:.

- Ստեղծեք պատկեր կոնկրետ կոնտեյներից.:

`docker {{[commit|container commit]}} {{container}} {{image}}:{{tag}}`

- Կիրառեք `CMD` Dockerfile հրահանգը ստեղծված պատկերին.:

`docker {{[commit|container commit]}} {{[-c|--change]}} "CMD {{command}}" {{container}} {{image}}:{{tag}}`

- Կիրառեք `ENV` Dockerfile հրահանգը ստեղծված պատկերին.:

`docker {{[commit|container commit]}} {{[-c|--change]}} "ENV {{name}}={{value}}" {{container}} {{image}}:{{tag}}`

- Ստեղծեք պատկեր կոնկրետ հեղինակի հետ մետատվյալներում.:

`docker {{[commit|container commit]}} {{[-a|--author]}} "{{author}}" {{container}} {{image}}:{{tag}}`

- Ստեղծեք պատկեր մետատվյալներում հատուկ մեկնաբանությունով.:

`docker {{[commit|container commit]}} {{[-m|--message]}} "{{comment}}" {{container}} {{image}}:{{tag}}`

- Ստեղծեք պատկեր առանց բեռնարկղը դադարեցնելու կատարման ընթացքում.:

`docker {{[commit|container commit]}} {{[-p|--pause]}} false {{container}} {{image}}:{{tag}}`

- Ցուցադրել օգնությունը.:

`docker {{[commit|container commit]}} --help`
