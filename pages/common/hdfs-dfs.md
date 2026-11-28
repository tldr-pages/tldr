# hdfs dfs

> Run filesystem commands on the Hadoop Distributed File System (HDFS).
> More information: <https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html>.

- List files and directories:

`hdfs dfs -ls {{path/to/directory}}`

- Create a directory and any missing parent directories:

`hdfs dfs -mkdir -p {{path/to/directory}}`

- Upload a local file to HDFS:

`hdfs dfs -put {{path/to/local_file}} {{path/to/remote_file}}`

- Download a file from HDFS to the local filesystem:

`hdfs dfs -get {{path/to/remote_file}} {{path/to/local_file}}`

- Display the contents of a file:

`hdfs dfs -cat {{path/to/file}}`

- Remove a file:

`hdfs dfs -rm {{path/to/file}}`

- Display the total size of a directory and its disk usage including replicas, in human-readable units:

`hdfs dfs -du -s -h {{path/to/directory}}`

- Display filesystem capacity, used space, and available space in human-readable units:

`hdfs dfs -df -h {{path/to/directory}}`
