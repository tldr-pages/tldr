# tarsnap-keygen

> Tarsnap, 온라인 백업 서비스에서 사용할 키 파일을 생성.
> 더 많은 정보: <https://www.tarsnap.com/man-tarsnap-keygen.1.html>.

- Tarsnap 서버에 컴퓨터 등록:

`sudo tarsnap-keygen --keyfile {{경로/대상/파일.key}} --user {{사용자_이메일}} --machine {{컴퓨터_이름}}`

- 키 파일 암호화(암호문을 두 번 입력해야 함):

`sudo tarsnap-keygen --keyfile {{경로/대상/파일.key}} --user {{사용자_이메일}} --machine {{컴퓨터_이름}} --passphrased`
