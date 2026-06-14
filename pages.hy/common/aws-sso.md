# aws sso

> Կառավարեք մուտքը դեպի AWS ռեսուրսներ՝ օգտագործելով Single Sign-On (SSO) հավատարմագրերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/sso/>:.

- Սկսեք SSO նիստը և թարմացրեք մուտքի նշանները: Պահանջվում է կարգավորում՝ օգտագործելով `aws configure sso`՝:

`aws sso login`

- Ավարտեք SSO նիստը և մաքրեք քեշավորված մուտքի նշանները.:

`aws sso logout`

- Թվարկեք բոլոր AWS հաշիվները, որոնք հասանելի են օգտագործողին.:

`aws sso list-accounts`

- Թվարկեք բոլոր դերերը, որոնք հասանելի են օգտվողին տվյալ AWS հաշվի համար.:

`aws sso list-account-roles --account-id {{account}} --access-token {{token}}`

- Առբերեք կարճաժամկետ հավատարմագրերը որոշակի հաշվի համար.:

`aws sso get-role-credentials --account-id {{account}} --role-name {{role}} --access-token {{token}}`
