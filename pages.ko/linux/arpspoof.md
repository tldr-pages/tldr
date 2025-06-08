# arpspoof

> 패킷을 가로채기 위해 ARP 응답을 위조합니다.
> 더 많은 정보: <https://manned.org/arpspoof>.

- 호스트의 패킷을 가로채기 위해 [i]인터페이스의 모든 호스트를 중독:

`sudo arpspoof -i {{wlan0}} {{호스트_IP}}`

- 호스트의 패킷을 가로채기 위해 [i]인터페이스의 [t]대상을 중독:

`sudo arpspoof -i {{wlan0}} -t {{대상_IP}} {{호스트_IP}}`

- 호스트의 패킷을 가로채기 위해 [i]인터페이스의 [t]대상과 호스트를 모두 중독:

`sudo arpspoof -i {{wlan0}} -r -t {{대상_IP}} {{호스트_IP}}`
