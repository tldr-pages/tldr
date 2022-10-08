# java

> जाभा अनुप्रयोग लन्चर.
> थप जानकारी: <https://docs.oracle.com/en/java/javase/17/docs/specs/man/java.html>.

- एउटा java `.class` फाइल कार्यान्वयन गर्नुहोस् जसमा क्लासको नाम प्रयोग गरेर मुख्य विधि समावेश हुन्छ:

`java {{classname}}`

- जाभा कार्यक्रम कार्यान्वयन गर्नुहोस् र थप तेस्रो-पक्ष वा प्रयोगकर्ता-परिभाषित कक्षाहरू प्रयोग गर्नुहोस्:

`java -classpath {{path/to/classes1}}:{{path/to/classes2}}:. {{classname}}`

- एक `.jar` कार्यक्रम कार्यान्वयन गर्नुहोस्:

`java -jar {{filename.jar}}`

- पोर्ट 5005 मा जडान हुनको लागि डिबगको साथ एक `.jar` कार्यक्रम कार्यान्वयन गर्नुहोस्:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{filename.jar}}`

- JDK, JRE र HotSpot संस्करणहरू प्रदर्शन गर्नुहोस्:

`java -version`

- जाभा आदेशको लागि प्रयोग जानकारी प्रदर्शन गर्नुहोस्:

`java -help`
