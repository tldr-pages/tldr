# cs resolve

> Resolve lists the transitive dependencies of one or more other dependencies.
> More information: <https://get-coursier.io/docs/cli-resolve>.

- Resolve lists of transitive dependencies of two dependencies:

`cs resolve {{group_id1}}:{{artifact_id1}}:{{artifact_version1}} {{group_id2}}:{{artifact_id2}}:{{artifact_version2}}`

- Resolve lists of transitive dependencies of a package by the dependency tree:

`cs resolve --tree {{groupId}}:{{artifactId}}:{{artifactVersion}}`

- Resolve dependency tree in a reverse order (from a dependency to its dependencies):

`cs resolve --reverse-tree {{groupId}}:{{artifactId}}:{{artifactVersion}}`

- Print all the libraries that depends on a particoular library:

`cs resolve {{groupId}}:{{artifactId}}:{{artifactVersion}} --what-depends-on {{searchedGroupId}}:{{searchedArtifactId}}`

- Print all the libraries that depends on a particoular library version:

`cs resolve {{groupId}}:{{artifactId}}:{{artifactVersion}} --what-depends-on {{searchedGroupId}}:{{searchedArtifactId}}{{searchedArtifactVersion}}`

- Print eventual conflits between a set of packages:

`cs resolve --conflicts {{groupId1}}:{{artifactId1}}:{{artifactartifactVersion1}} {{groupId2}}:{{artifactId2}}:{{artifactVersion2}}} {{groupId3}}:{{artifactId3}}:{{artifactVersion3}}`
