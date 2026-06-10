# openvpn

> OpenVPN հաճախորդ և դեյմոն երկուական:.
> Լրացուցիչ տեղեկություններ. <https://openvpn.net/community-docs/community-articles/openvpn-2-6-manual.html>:.

- Միացեք սերվերին, օգտագործելով կազմաձևման ֆայլը.:

`sudo openvpn {{path/to/client.conf}}`

- Փորձեք ստեղծել անապահով peer-to-peer թունել bob.example.com հոսթի վրա.:

`sudo openvpn --remote {{alice.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.1}} {{10.4.0.2}}`

- Միացեք սպասող bob.example.com հոսթին առանց գաղտնագրման.:

`sudo openvpn --remote {{bob.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.2}} {{10.4.0.1}}`

- Ստեղծեք ծածկագրային բանալի և պահեք այն ֆայլում.:

`openvpn --genkey secret {{path/to/key}}`

- Փորձեք ստեղծել «peer-to-peer» թունել bob.example.com հոսթի վրա ստատիկ բանալիով.:

`sudo openvpn --remote {{alice.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.1}} {{10.4.0.2}} --secret {{path/to/key}}`

- Միացեք սպասող bob.example.com հոսթին նույն ստատիկ ստեղնով, ինչ bob.example.com-ում:

`sudo openvpn --remote {{bob.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.2}} {{10.4.0.1}} --secret {{path/to/key}}`
