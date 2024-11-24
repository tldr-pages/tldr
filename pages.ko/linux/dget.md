# dget

> Debian 패키지 다운로드.
> 더 많은 정보: <https://manned.org/dget.1>.

- 바이너리 패키지 다운로드:

`dget {{패키지}}`

- `.dsc` 파일에서 패키지 소스를 다운로드하고 추출:

`dget {{http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc}}`

- `.dsc` 파일에서 패키지 소스 tarball을 다운로드하지만 추출하지 않음:

`dget -d {{http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc}}`
