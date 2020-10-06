# java

> ஜாவா பயன்பாட்டு துவக்கி.
> மேலும் தகவலுக்கு: <https://java.com>.

- ஒரு main செயல்பாட்டைக் கொண்ட ஜாவா .class கோப்பை வெறும் class பெயரை பயன்படுத்தி இயக்கவும்:

`java {{classname}}`

- ஒரு .jar நிரலை இயக்கவும்:

`java -jar {{filename.jar}}`

- போர்ட் 5005 இல் இணைக்க காத்திருக்கும் பிழைதிருத்தி .jar நிரலை இயக்கவும்:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{filename.jar}}`

- JDK, JRE மற்றும் HotSpot மென்பொருள் பதிப்புகள் காண்பி:

`java -version`

- java கட்டளைக்கான பயன்பாட்டு தகவலை காண்பி:

`java -help`
