# oauth2c

> Փոխազդեք OAuth 2.0 թույլտվության սերվերների հետ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/cloudentity/oauth2c#usage>:.

- Ստացեք մուտքի նշան՝ օգտագործելով հաճախորդի հավատարմագրերը.:

`oauth2c {{issuer_url}} --client-id {{client_id}} --client-secret {{client_secret}}`

- Ստացեք նշան՝ օգտագործելով թույլտվության կոդի հոսքը.:

`oauth2c {{issuer_url}} --client-id {{client_id}} --response-types code`

- Ստացեք նշան՝ օգտագործելով PKCE-ի թույլտվության կոդը.:

`oauth2c {{issuer_url}} --client-id {{client_id}} --pkce`

- Ստացեք նշան՝ օգտագործելով գաղտնաբառի հավատարմագրերը.:

`oauth2c {{issuer_url}} --client-id {{client_id}} --username {{username}} --password {{password}}`

- Թարմացրեք առկա մուտքի նշանը.:

`oauth2c {{issuer_url}} --client-id {{client_id}} --refresh-token {{refresh_token}}`

- Ստացեք նշան հատուկ շրջանակներով.:

`oauth2c {{issuer_url}} --client-id {{client_id}} --scopes {{scope1,scope2}}`

- Օգտագործեք սարքի թույլտվության հոսքը.:

`oauth2c {{issuer_url}} --client-id {{client_id}} --grant-type device_code`

- Գործարկել լուռ ռեժիմով առանց բրաուզերի.:

`oauth2c {{issuer_url}} --client-id {{client_id}} {{[-s|--silent]}} --no-browser`
