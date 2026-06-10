# ուղարկել նամակ

> Ուղարկել էլ.
> Լրացուցիչ տեղեկություններ. <https://manned.org/sendmail>:.

- Ուղարկեք `message.txt` բովանդակությամբ հաղորդագրություն տեղական օգտագործողի `username` փոստի գրացուցակին:

`sendmail < {{message.txt}} {{username}}`

- Ուղարկեք նամակ `sender@example.com`-ից (ենթադրելով, որ փոստային սերվերը կազմաձևված է դրա համար) `receiver@example.com` հասցեին, որը պարունակում է հաղորդագրություն `message.txt`-ում.:

`sendmail < message.txt -f sender@example.com receiver@example.com`

- Ուղարկեք նամակ `sender@example.com`-ից (ենթադրելով, որ փոստային սերվերը կազմաձևված է դրա համար) `receiver@example.com` հասցեին, որը պարունակում է `file.zip` ֆայլը:

`sendmail < file.zip -f sender@example.com receiver@example.com`
