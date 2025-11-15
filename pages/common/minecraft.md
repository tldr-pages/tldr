# Minecraft

> Run a headless Minecraft server.
> More information: <https://minecraft.wiki/w/Tutorial:Setting_up_a_Java_Edition_server>.

- Start a Minecraft server and generate a world if it doesn't exist:

`java -jar {{path/to/server.jar}} --nogui`

- Set the minimum and maximum amount of memory a server is allowed to have (Note: Setting them the same prevents lag caused by heap scaling):

`java -Xms{{1024M}} -Xmx{{2048M}} -jar {{path/to/server.jar}} --nogui`

- Start a server with a GUI:

`java -jar {{path/to/server.jar}}`

- Shut the server down:

`stop`
