# magento

> Magento PHP 프레임워크 관리.
> 더 많은 정보: <https://experienceleague.adobe.com/en/docs/commerce-operations/tools/cli-reference/commerce-on-premises>.

- 하나 이상의 모듈 활성화:

`magento module:enable {{모듈1 모듈2 ...}}`

- 하나 이상의 모듈 비활성화:

`magento module:disable {{모듈1 모듈2 ...}}`

- 모듈 활성화 후 데이터베이스 업데이트:

`magento setup:upgrade`

- 코드 및 의존성 주입 구성 업데이트:

`magento setup:di:compile`

- 정적 에셋 배포:

`magento setup:static-content:deploy`

- 유지보수 모드 활성화:

`magento maintenance:enable`

- 유지보수 모드 비활성화:

`magento maintenance:disable`

- 사용 가능한 모든 명령 나열:

`magento list`
