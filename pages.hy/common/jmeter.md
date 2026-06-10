# jmeter

> Բաց կոդով Java հավելված, որը նախատեսված է բեռնվածության փորձարկման ֆունկցիոնալ վարքագծի և կատարողականությունը չափելու համար:.
> Լրացուցիչ տեղեկություններ. <https://jmeter.apache.org/usermanual/get-started.html#options>:.

- Գործարկեք հատուկ թեստային պլան nongui ռեժիմով.:

`jmeter {{[-n|--nongui]}} {{[-t|--testfile]}} {{path/to/file.jmx}}`

- Գործարկեք թեստային պլան nongui ռեժիմում, օգտագործելով հատուկ գրանցամատյան ֆայլ.:

`jmeter {{[-n|--nongui]}} {{[-t|--testfile]}} {{path/to/file.jmx}} {{[-l|--logfile]}} {{path/to/logfile.jtl}}`

- Գործարկեք թեստային պլան ոչ գուի ռեժիմում՝ օգտագործելով հատուկ վստահված անձ.:

`jmeter {{[-n|--nongui]}} {{[-t|--testfile]}} {{path/to/file.jmx}} {{[-H-|--proxyHost]}} {{127.0.0.1}} {{[-P|--proxyPort]}} {{8888}}`

- Գործարկեք թեստային պլան nongui ռեժիմում՝ օգտագործելով հատուկ JMeter հատկություն.:

`jmeter {{[-n|--nongui]}} {{[-t|--testfile]}} {{path/to/file.jmx}} {{[-J|--jmeterproperty]}} {{key}}='{{value}}'`
