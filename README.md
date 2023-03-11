# mimir

companion to heimball, this tool sources and wrangles data from various sources, brings them together,
and sends them off to heimball via the graphql API.

## todo:

- remove some unused code
- get some better organization up in this
- populate `active`, `currentTeamId` and `parentOrgId` fields from the MLB API.

## how to:

interface with the tool should be done by running `mimir.py`.

at the moment, there are a couple of actions that exist in the `mimir.py` file.

to source the data, use `execute_upload()` - better name coming. this will download the retrosheet CSVs,
extend them with the MLB API (to a certain degree), and then ship the data off to the heimball API.
