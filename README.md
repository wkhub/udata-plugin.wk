# udata-plugin wk template

A [wk](https://github.com/wkhub/wk) template for a [uData](https://getudata.org) package (containing one or more plugin)

## Usage

```
wk mix gh:wkhub/udata-plugin.wk
```

Provide the requested informations and then you can go in the newly created directory
(which will be the `project_slug` that you provided).


## Fields

These are the fields used by this cookiecutter template:

- **`project_name`**: The project name that will also serve as Backend display name (ex: `My Harvester`)
- **`project_slug`**: The project slug used as root folder name (ex: `udata-my-harvester`)
- **`pypackage`**: The project root package name (ex: `udata_my_harvester`)
- **`identifier`**: The backend entrypoint identifier (ex: `mine`)
- **`license`**: The license under which the project is published (ex: `AGPL`)
- **`author`**: The project author (ex: `OpenDataTeam`)
- **`email`**: The project contact email (ex: `contact@opendata.team`)
- **`description`**: The project short description (ex: `My awesome uData harvester`)
- **`version`**: The initial version (ex: `0.1.0.dev`)
- **`website`**: The project website (ex: `https://github.com/opendatateam/udata-my-harvester`)
- **`features`**: A set of selected features to enable
    - **`harvester`**`: Adds a harvester skeleton (see the [udata harvesting documention](https://udata.readthedocs.io/en/stable/harvesting/))
    - **`theme`**: Adds a theme skeleton (see the [udata theming documention](https://udata.readthedocs.io/en/stable/creating-theme/))
    - **`views`**: Adds a views skeleton
    - **`metrics`**: Adds a metrics skeleton
    - **`models`**: Adds a models skeleton
    - **`linkchecker`**: Adds a linkchecker skeleton
    - **`tasks`**: Adds a tasks skeleton
    - **`preview`**`: Adds a preview plugin skeleton
    - **`generic`**: Adds a generic plugin skeleton
