# sniff.py

> `pcapy` 라이브러리를 사용해 네트워크 패킷을 캡처하고 표시.
> Impacket 도구 모음의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- 사용 가능한 네트워크 인터페이스 목록을 표시하고 하나를 선택해 패킷 캡처를 시작 (`sudo` 권한 필요):

`sudo sniff.py`

- 패킷을 캡처하면서 터미널에 표시하고, 동시에 출력파일에 저장:

`sudo sniff.py | sudo tee {{경로/대상/출력_파일}}`
