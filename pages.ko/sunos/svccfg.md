# svccfg

> 서비스 구성을 가져오고, 내보내고, 수정합니다.
> 더 많은 정보: <https://www.unix.com/man-page/linux/1m/svccfg>.

- 구성 파일 유효성 검사:

`svccfg validate {{경로/대상/smf_파일.xml}}`

- 서비스 구성을 파일로 내보내기:

`svccfg export {{서비스명}} > {{경로/대상/smf_파일.xml}}`

- 파일에서 서비스 구성 가져오거나 업데이트:

`svccfg import {{경로/대상/smf_파일.xml}}`
