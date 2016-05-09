# Esdeploy

Zero-Downtime Elasticsearch index deployer

This project was created to put elasticsearch indices in source control and deploy them with in a simple workflow

Usage:
------------
**esdeploy configure**  
Prompts information for initial server configuration

**esdeploy init [index_name]**  
Initializes the index for the workflow, which means reading it, storing it as json. Migrating it and adding an alias to it.

**esdeploy deploy [index_name]**  
Deploys the index with matching json file in the working directory. It creates the index, migrates data and moves the alias to it.

Caveats:
------------
* Indices shouldn't have an alias prior to init
* Only supports a single alias per index
