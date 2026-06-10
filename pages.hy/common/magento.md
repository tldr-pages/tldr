#magento

> Կառավարեք Magento PHP շրջանակը:.
> Լրացուցիչ տեղեկություններ. <https://experienceleague.adobe.com/en/docs/commerce-operations/tools/cli-reference/commerce-on-premises>:.

- Միացնել մեկ կամ մի քանի մոդուլ.:

`magento module:enable {{module1 module2 ...}}`

- Անջատել մեկ կամ մի քանի մոդուլ.:

`magento module:disable {{module1 module2 ...}}`

- Թարմացրեք տվյալների բազան մոդուլները միացնելուց հետո.:

`magento setup:upgrade`

- Թարմացրեք կոդը և կախվածության ներարկման կոնֆիգուրացիան.:

`magento setup:di:compile`

- Տեղադրել ստատիկ ակտիվներ.:

`magento setup:static-content:deploy`

- Միացնել պահպանման ռեժիմը.:

`magento maintenance:enable`

- Անջատել սպասարկման ռեժիմը.:

`magento maintenance:disable`

- Թվարկեք բոլոր հասանելի հրամանները.:

`magento list`
