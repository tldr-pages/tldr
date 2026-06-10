# aws-google-auth

> Ձեռք բերեք AWS-ի ժամանակավոր (STS) հավատարմագրեր՝ օգտագործելով Google Apps-ը որպես դաշնային (Single Sign-On) մատակարար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/cevoaustralia/aws-google-auth>:.

- Մուտք գործեք Google SSO-ով` օգտագործելով նշված օգտվողի անունը IDP և SP նույնացուցիչները և սահմանեք հավատարմագրերի տևողությունը մեկ ժամ.:

`aws-google-auth {{[-u|--username]}} {{example@example.com}} {{[-I|--idp-id]}} {{$GOOGLE_IDP_ID}} {{[-S|--sp-id]}} {{$GOOGLE_SP_ID}} {{[-d|--duration]}} {{3600}}`

- Մուտք գործեք՝ հարցնելով, թե որ դերն օգտագործել (մի քանի մատչելի SAML դերերի դեպքում).:

`aws-google-auth {{[-u|--username]}} {{example@example.com}} {{[-I|--idp-id]}} {{$GOOGLE_IDP_ID}} {{[-S|--sp-id]}} {{$GOOGLE_SP_ID}} {{[-d|--duration]}} {{3600}} {{[-a|--ask-role]}}`

- Լուծեք AWS հաշիվների փոխանունները.:

`aws-google-auth {{[-u|--username]}} {{example@example.com}} {{[-I|--idp-id]}} {{$GOOGLE_IDP_ID}} {{[-S|--sp-id]}} {{$GOOGLE_SP_ID}} {{[-d|--duration]}} {{3600}} {{[-a|--ask-role]}} --resolve-aliases`

- Ցուցադրել օգնությունը.:

`aws-google-auth {{[-h|--help]}}`
