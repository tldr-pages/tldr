# հավաքել ինտել

> Հավաքեք բաց կոդով ինտել այնպիսի կազմակերպությունների վրա, ինչպիսիք են արմատային տիրույթները և ASN-ները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-intel-subcommand>:.

- Գտեք արմատային տիրույթներ IP [addr]ess տիրույթում.:

`amass intel -addr {{192.168.0.1-254}}`

- Օգտագործեք ակտիվ վերահաշվարկի մեթոդներ.:

`amass intel -active -addr {{192.168.0.1-254}}`

- Գտեք արմատային տիրույթներ՝ կապված [d]տիրույթի հետ.:

`amass intel -whois -d {{domain_name}}`

- Գտեք [կազմակերպ] կազմակերպությանը պատկանող ASN-ներ.:

`amass intel -org {{organisation_name}}`

- Գտեք արմատային տիրույթներ, որոնք պատկանում են տվյալ ինքնավար համակարգի համարին.:

`amass intel -asn {{asn}}`

- Պահպանեք արդյունքները տեքստային ֆայլում.:

`amass intel -o {{output_file}} -whois -d {{domain_name}}`

- Թվարկեք բոլոր առկա տվյալների աղբյուրները.:

`amass intel -list`
