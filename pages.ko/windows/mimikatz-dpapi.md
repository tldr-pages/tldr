# mimikatz dpapi

> Windows Data Protection API (DPAPI)와 상호작용.
> 더 많은 정보: <https://github.com/gentilkiwi/mimikatz>.

- 마스터 키 목록 표시:

`mimikatz "dpapi::masterkey /list"`

- DPAPI blob 복호화:

`mimikatz "dpapi::blob /in:blob_file.bin"`

- DPAPI를 사용하여 Chrome 자격 증명 가져오기:

`mimikatz "dpapi::chrome /in:Login Data"`
