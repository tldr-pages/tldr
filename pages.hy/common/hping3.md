# hping3

> Ընդլայնված ping կոմունալ, որն աջակցում է այնպիսի արձանագրությունների, ինչպիսիք են TCP, UDP և հում IP-ն:.
> Լավագույն վազքը բարձր արտոնություններով:.
> Տես նաև՝ `masscan`, `naabu`, `nmap`, `rustscan`, `zmap`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/hping3>:.

- Ping ուղղություն 4 ICMP ping հարցումով.:

`hping3 {{[-1|--icmp]}} {{[-c|--count]}} 4 {{ip_or_hostname}}`

- Ping IP հասցե UDP-ի միջոցով 80 նավահանգստում.:

`hping3 {{[-2|--udp]}} {{[-p|--destport]}} 80 {{[-S|--syn]}} {{ip_or_hostname}}`

- Սկանավորեք TCP 80 նավահանգիստը, սկանավորելով տեղական աղբյուրի հատուկ պորտից 5090:

`hping3 {{[-V|--verbose]}} {{[-S|--syn]}} {{[-p|--destport]}} 80 {{[-s|--baseport]}} 5090 {{ip_or_hostname}}`

- Traceroute օգտագործելով TCP սկան դեպի որոշակի նպատակակետ նավահանգիստ.:

`hping3 {{[-T|--traceroute]}} {{[-V|--verbose]}} {{[-S|--syn]}} {{[-p|--destport]}} {{80}} {{ip_or_hostname}}`

- Սկանավորեք մի շարք TCP նավահանգիստներ որոշակի IP հասցեի վրա.:

`hping3 {{[-8|--scan]}} {{80,3000,9000}} {{[-S|--syn]}} {{ip_or_hostname}}`

- Կատարեք TCP ACK սկան՝ ստուգելու համար, թե արդյոք տվյալ հյուրընկալողը կենդանի է.:

`hping3 {{[-c|--count]}} {{2}} {{[-V|--verbose]}} {{[-p|--destport]}} {{80}} {{[-A|--ack]}} {{ip_or_hostname}}`

- Կատարեք լիցքավորման փորձարկում 80 նավահանգստի վրա.:

`hping3 --flood {{[-p|--destport]}} 80 {{[-S|--syn]}} {{ip_or_hostname}}`
