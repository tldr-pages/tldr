# hdfs

> Manage the Hadoop Distributed File System (HDFS).
> Some subcommands such as `dfs` have their own usage documentation.
> More information: <https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HDFSCommands.html>.

- View documentation for filesystem commands:

`tldr hdfs dfs`

- List files and directories in HDFS:

`hdfs dfs -ls {{path/to/directory}}`

- Display filesystem statistics and DataNode information:

`hdfs dfsadmin -report`

- Display the value of a configuration key:

`hdfs getconf -confKey {{configuration_key}}`

- Display help for filesystem commands:

`hdfs dfs -help`

- Display version:

`hdfs version`
