# gpgv

> OpenPGP 서명을 확인.
> 더 많은 정보: <https://www.gnupg.org/documentation/manuals/gnupg/gpgv.html>.

- 서명된 파일을 확인:

`gpgv {{경로/대상/파일}}`

- 분리된 서명을 사용하여 서명된 파일을 확인:

`gpgv {{경로/대상/서명}} {{경로/대상/파일}}`

- 키링 목록에 파일을 추가 (내보낸 단일 키도 키링으로 간주됨):

`gpgv --keyring {{./alice.keyring}} {{경로/대상/서명}} {{경로/대상/파일}}`
