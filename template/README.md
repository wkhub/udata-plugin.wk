# {{ .ctx.project_name }}

{{ .ctx.description }}

## Usage

Install the plugin package in you udata environement:

```bash
pip install {{ .ctx.project_slug }}
```

Then activate it in your `udata.cfg`:

```python
PLUGINS = ['{{ .ctx.project_slug }}']
```
