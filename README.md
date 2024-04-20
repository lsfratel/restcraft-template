# RestCraft Template

This is a template for creating a ResCraft project.

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

## Use this template
To use this template rename the `restcraft_app` to your project name, then edit the `settings.py` and the `__init__.py`.

```python
# your_project_name/settings.py
VIEWS = {
    "YOUR_PROJECT_NAME.views.my_view",
}

# your_project_name/__init__.py
os.environ.setdefault('RESTCRAFT_SETTINGS_MODULE', 'YOUR_PROJECT_NAME.settings')
```

or you can use this one line command:

```bash
# Run this command inside the clonned template
mv restcraft_app YOUR_PROJECT_NAME && find . -type f -exec sed -i 's/restcraft_app/YOUR_PROJECT_NAME/g' {} +
```

Then install the dependencies.
```bash
pdm install
```

# Scripts
Here are some scripts that you can use:

```bash
# Start the development server with automatic reload.
pdm dev
```

```bash
# Unittesting
pdm test
```
