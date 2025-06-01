# pamshadedrelief

> 고도 지도를 사용하여 음영 지형도를 생성.
> 같이 보기: `pamcrater`, `ppmrelief`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pamshadedrelief.html>.

- 입력 이미지를 고도 지도로 해석하여 음영 지형도 이미지 생성:

`pamshadedrelief < {{경로/대상/입력.pam}} > {{경로/대상/출력.pam}}`

- 지정된 계수로 이미지 감마 조정:

`pamshadedrelief {{[-g|-gamma]}} {{계수}} < {{경로/대상/입력.pam}} > {{경로/대상/출력.pam}}`
