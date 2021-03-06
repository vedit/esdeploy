# Esdeploy

Zero-Downtime Elasticsearch index deployer

This project was created to put elasticsearch indices in source control and deploy them with in a simple workflow

Usage:
------------
**esdeploy configure**  
Prompts information for initial server configuration

**esdeploy init [index_name]**  
Initializes the index for the workflow. If the index exists on the server, stores mapping and settings as json. Migrating it and adding an alias to it. If the index doesn't exist, it searches for a matching file to create and initialize.

**esdeploy deploy [index_name]**  
Deploys the index with matching json file in the working directory. It creates the index, migrates data and moves the alias to it.

Intended Workflow
-------------
Annotating the following chart; esindices is the repository folder and the subdirectories are created per-environment basis. Each shoud be configured with the command `esdeploy configure` and used accordingly. 
```
esindices
├── sb
│   ├── index_a.json
│   ├── index_b.json
│   └── esdeploy.json
├── qa
│   ├── index_a.json
│   ├── index_b.json
│   └── esdeploy.json
└── stg
    ├── index_a.json
    ├── index_b.json
    └── esdeploy.json
```

Caveats:
------------
* Indices shouldn't have an alias prior to init
* Only supports a single alias per index
