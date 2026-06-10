# fdroid

> F-Droid կառուցման գործիք:.
> F-Droid-ը FOSS (անվճար և բաց կոդով ծրագրակազմ) հավելվածների տեղադրվող կատալոգ է Android պլատֆորմի համար:.
> Լրացուցիչ տեղեկություններ. <https://f-droid.org/en/docs/Building_Applications/>:.

- Ստեղծեք հատուկ հավելված.:

`fdroid build {{app_id}}`

- Ստեղծեք հատուկ հավելված build server VM-ում.:

`fdroid build {{app_id}} --server`

- Հրապարակեք հավելվածը տեղական պահեստում.:

`fdroid publish {{app_id}}`

- Տեղադրեք հավելվածը յուրաքանչյուր միացված սարքի վրա.:

`fdroid install {{app_id}}`

- Ստուգեք, արդյոք մետատվյալները ճիշտ ձևաչափված են.:

`fdroid lint --format {{app_id}}`

- Ինքնաբերաբար շտկել ձևաչափումը (եթե հնարավոր է).:

`fdroid rewritemeta {{app_id}}`
