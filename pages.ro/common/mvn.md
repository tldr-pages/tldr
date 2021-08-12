# mvn

> Apache Maven.
> Instrument pentru construirea și gestionarea proiectelor bazate pe Java.
> Mai multe informaţii: <https://maven.apache.org>

- Compilarea unui proiect:

`mvn compile`

- Compilarea și ambalarea codului compilat în formatul său distribuibil, cum ar fi un `jar':

`mvn package`

- Compilarea și ambalarea, sărind peste testele unității:

`mvn package -Dmaven.test.skip=true`

- Instalați pachetul construit în depozitul local de maven. (Aceasta va invoca și comenzile de compilare și pachet):

`mvn install`

- Ștergeți artefactele construi din directorul țintă:

`mvn clean`

- Faceți o curățare și apoi invocați faza pachetului:

`mvn clean package`

- Curățați și apoi împachetați codul cu un anumit profil de construire:

`mvn clean -P{{profile}} package`

- Rulați o clasă cu o metodă principală:

`mvn exec:java -Dexec.mainClass="{{com.example.Main}}" -Dexec.args="{{arg1 arg2}}"`
