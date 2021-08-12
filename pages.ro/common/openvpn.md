# openvpn

> client OpenVPN și binar daemon.
> Mai multe informaţii: <https://openvpn.net/>

- Conectați-vă la server utilizând un fișier de configurare:

`sudo openvpn {{path/to/client.conf}}`

- Încercați să configurați un tunel peer-to-peer nesigur pe bob.example.com gazdă:

`sudo openvpn --remote {{alice.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.1}} {{10.4.0.2}}`

- Conectați-vă la gazda bob.example.com care așteaptă fără criptare:

`sudo openvpn --remote {{bob.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.2}} {{10.4.0.1}}`

- Creați o cheie criptografică și salvați-o în fișier:

`openvpn --genkey --secret {{path/to/key}}`

- Încercați să configurați un tunel peer-to-peer pe bob.example.com gazdă cu o cheie statică:

`sudo openvpn --remote {{alice.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.1}} {{10.4.0.2}} --secret {{path/to/key}}`

- Conectați-vă la gazda bob.example.com care așteaptă cu aceeași cheie statică ca pe bob.example.com:

`sudo openvpn --remote {{bob.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.2}} {{10.4.0.1}} --secret {{path/to/key}}`
