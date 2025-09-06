# dpkg-deb

> Debian 아카이브를 패키징, 압축 해제 및 정보 제공.
> 더 많은 정보: <https://manned.org/dpkg-deb>.

- 패키지 정보 표시:

`dpkg-deb --info {{경로/대상/파일.deb}}`

- 패키지의 이름과 버전을 한 줄로 표시:

`dpkg-deb --show {{경로/대상/파일.deb}}`

- 패키지의 내용 나열:

`dpkg-deb --contents {{경로/대상/파일.deb}}`

- 패키지의 내용을 디렉토리에 추출:

`dpkg-deb --extract {{경로/대상/파일.deb}} {{경로/대상/폴더}}`

- 지정된 디렉토리에서 패키지 생성:

`dpkg-deb --build {{경로/대상/폴더}}`
