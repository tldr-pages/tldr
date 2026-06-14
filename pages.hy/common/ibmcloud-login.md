# ibmcloud մուտք

> Մուտք գործեք IBM Cloud:.
> Լրացուցիչ տեղեկություններ. <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login>:.

- Մուտք գործեք՝ օգտագործելով ինտերակտիվ հուշում.:

`ibmcloud login`

- Մուտք գործեք որոշակի API վերջնակետ (կանխադրվածը `cloud.ibm.com` է):

`ibmcloud login -a {{api_endpoint}}`

- Մուտք գործեք՝ որպես պարամետրեր տրամադրելով օգտվողի անունը, գաղտնաբառը և թիրախային տարածաշրջանը.:

`ibmcloud login -u {{username}} -p {{password}} -r {{us-south}}`

- Մուտք գործեք API բանալիով, փոխանցելով այն որպես փաստարկ.:

`ibmcloud login --apikey {{api_key_string}}`

- Մուտք գործեք API բանալիով, այն փոխանցելով որպես ֆայլ.:

`ibmcloud login --apikey @{{path/to/api_key_file}}`

- Մուտք գործեք դաշնային ID-ով (մեկ գրանցում).:

`ibmcloud login --sso`
