# ssh-keyscan

> Ստացեք հեռակառավարվող հոսթերների հանրային SSH ստեղները:.
> Լրացուցիչ տեղեկություններ. <https://man.openbsd.org/ssh-keyscan>:.

- Առբերեք հեռավոր հոսթի բոլոր հանրային SSH ստեղները.:

`ssh-keyscan {{hostname}}`

- Առբերեք հեռավոր հոսթի բոլոր հանրային SSH ստեղները, որոնք լսում են որոշակի նավահանգիստ.:

`ssh-keyscan -p {{port}} {{hostname}}`

- Առբերեք հեռավոր հոսթի որոշ տեսակի հանրային SSH ստեղներ.:

`ssh-keyscan -t {{rsa,dsa,ecdsa,ed25519}} {{hostname}}`

- Ձեռքով թարմացրեք SSH known_hosts ֆայլը տվյալ հոսթի մատնահետքով.:

`ssh-keyscan -H {{hostname}} >> ~/.ssh/known_hosts`
