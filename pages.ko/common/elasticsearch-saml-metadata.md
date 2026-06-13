# elasticsearch-saml-metadata

> SAML Identity Provider 구성을 위한 SAML Service Provider 메타데이터를 생성하는 도구.
> 더 많은 정보: <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/saml-metadata>.

- 특정 realm에 대한 SAML 메타데이터를 생성하고 `stdout`으로 출력:

`elasticsearch-saml-metadata --realm {{realm_이름}}`

- SAML 메타데이터를 생성하여 특정 파일로 저장:

`elasticsearch-saml-metadata --realm {{realm_이름}} --out {{경로/대상/파일.xml}}`

- 도움말 표시:

`elasticsearch-saml-metadata {{[-h|--help]}}`
