# ldapsearch

> LDAP 디렉토리를 쿼리.
> 더 많은 정보: <https://docs.ldap.com/ldap-sdk/docs/tool-usages/ldapsearch.html>.

- 주어진 그룹의 멤버인 모든 항목을 LDAP 서버에서 쿼리하고 객체의 displayName 값을 반환:

`ldapsearch -D '{{관리자_DN}}' -w '{{비밀번호}}' -h {{ldap_호스트}} -b {{기본_ou}} '{{memberOf=group1}}' displayName`

- 줄바꿈 없는 비밀번호 파일을 사용하여 주어진 그룹의 멤버인 모든 항목을 LDAP 서버에서 쿼리하고 객체의 displayName 값을 반환:

`ldapsearch -D '{{관리자_DN}}' -y '{{비밀번호_파일}}' -h {{ldap_호스트}} -b {{기본_ou}} '{{memberOf=group1}}' displayName`

- 주어진 필터에 맞는 5개의 항목 반환:

`ldapsearch -D '{{관리자_DN}}' -w '{{비밀번호}}' -h {{ldap_호스트}} -b {{기본_ou}} '{{memberOf=group1}}' -z 5 displayName`

- 응답을 최대 7초 동안 대기:

`ldapsearch -D '{{관리자_DN}}' -w '{{비밀번호}}' -h {{ldap_호스트}} -b {{기본_ou}} '{{memberOf=group1}}' -l 7 displayName`

- 필터 반전:

`ldapsearch -D '{{관리자_DN}}' -w '{{비밀번호}}' -h {{ldap_호스트}} -b {{기본_ou}} '(!(memberOf={{group1}}))' displayName`

- 여러 그룹에 속한 모든 항목을 반환하고 각 항목의 display name 반환:

`ldapsearch -D '{{관리자_DN}}' -w '{{비밀번호}}' -h {{ldap_호스트}} '(&({{memberOf=group1}})({{memberOf=group2}})({{memberOf=group3}}))' "displayName"`

- 지정된 그룹 중 적어도 1개에 속한 모든 항목 반환:

`ldapsearch -D '{{관리자_DN}}' -w '{{비밀번호}}' -h {{ldap_호스트}} '(|({{memberOf=group1}})({{memberOf=group1}})({{memberOf=group3}}))' displayName`

- 여러 부울 논리 필터 결합:

`ldapsearch -D '{{관리자_DN}}' -w '{{비밀번호}}' -h {{ldap_호스트}} '(&({{memberOf=group1}})({{memberOf=group2}})(!({{memberOf=group3}})))' displayName`
