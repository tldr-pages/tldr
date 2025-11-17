# wp

> WordPress 인스턴스를 관리하는 공식 명령줄 인터페이스.
> 더 많은 정보: <https://developer.wordpress.org/cli/commands/>.

- 운영 체제, 셸, PHP 및 WP-CLI(`wp`) 설치 정보 출력:

`wp --info`

- WP-CLI 업데이트:

`wp cli update`

- 현재 디렉토리에 새로운 WordPress 설치 파일 다운로드, 필요시 로케일 지정:

`wp core download --locale={{로케일}}`

- 기본 `wpconfig` 파일 생성 (데이터베이스가 `localhost`에 있다고 가정):

`wp config create --dbname={{데이터베이스_이름}} --dbuser={{데이터베이스_사용자}} --dbpass={{데이터베이스_비밀번호}}`

- WordPress 플러그인 설치 및 활성화:

`wp plugin install {{플러그인}} --activate`

- 데이터베이스에서 문자열의 모든 인스턴스 교체:

`wp search-replace {{기존_문자열}} {{새로운_문자열}}`

- WordPress 확장 RSS(WXR) 파일의 내용 가져오기:

`wp import {{경로/대상/파일.xml}}`
