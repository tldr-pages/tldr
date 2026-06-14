#սոկատ

> Բազմաֆունկցիոնալ ռելե (SOcket CAT):.
> Լրացուցիչ տեղեկություններ. <http://www.dest-unreach.org/socat/>:.

- Լսեք մի նավահանգիստ, սպասեք մուտքային կապի և տվյալները փոխանցեք STDIO-ին.:

`sudo socat - TCP-LISTEN:8080,fork`

- Լսեք նավահանգստում SSL-ի միջոցով և տպեք `stdout`-ով:

`sudo socat OPENSSL-LISTEN:4433,reuseaddr,cert=./cert.pem,cafile=./ca.cert.pem,key=./key.pem,verify=0 STDOUT`

- Ստեղծեք կապ հոսթի և նավահանգստի հետ, փոխանցեք տվյալները STDIO-ում միացված հոսթին.:

`sudo socat - TCP4:www.example.com:80`

- Փոխանցել տեղական նավահանգստի մուտքային տվյալները մեկ այլ հոսթ և նավահանգիստ.:

`sudo socat TCP-LISTEN:80,fork TCP4:www.example.com:80`

- Ուղարկեք տվյալներ multicast երթուղավորման սխեմայով.:

`{{echo "Hello Multicast"}} | socat - UDP4-DATAGRAM:{{224.0.0.1}}:{{5000}}`

- Ստացեք տվյալներ multicast-ից.:

`socat - UDP4-RECVFROM:{{5000}}`
