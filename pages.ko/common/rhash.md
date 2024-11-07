# rhash

> 일반적인 메시지 다이제스트를 계산하거나 확인.
> 더 많은 정보: <https://rhash.sourceforge.net/manpage.php>.

- 파일의 기본 CRC32 다이제스트 계산:

`rhash {{경로/대상/파일}}`

- 디렉터리를 재귀적으로 처리하여 SHA1을 사용한 SFV 파일 생성:

`rhash --sha1 --recursive {{경로/대상/폴더}} > {{경로/대상/출력.sfv}}`

- SFV 파일을 기반으로 파일의 무결성 확인:

`rhash --check {{경로/대상/파일.sfv}}`

- 텍스트 메시지의 SHA3 다이제스트 계산:

`rhash --sha3-256 --message '{{메시지}}'`

- 파일의 CRC32 다이제스트를 계산하고 BSD 형식을 사용하여 base64로 인코딩된 다이제스트 출력:

`rhash --base64 --bsd {{경로/대상/파일}}`

- 사용자 정의 출력 템플릿 사용:

`rhash --printf '{{%p\t%s\t%{mtime}\t%m\n}}' {{경로/대상/파일}}`
