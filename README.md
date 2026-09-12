# GHIV Africa SCI-NHF Kobo Live Dashboard v2

Configured for the combined Kobo project:
- EU server: https://eu.kobotoolbox.org
- Asset UID: ajcMeB4nsHXPoSdvbwGxRH

## Secure setup
Set KOBO_API_TOKEN on the server/hosting platform. Do not put the key in dashboard.html or commit it to GitHub.

## Local run
pip install -r requirements.txt
Set the environment variables from .env.example
python app.py
Then open http://localhost:5000

## Live behaviour
The dashboard refreshes automatically every 5 minutes and also has a manual Refresh Data button.

## Deployment
Deploy this folder to a Python-capable service such as Render, Railway, PythonAnywhere, or your organization's server. Add the three environment variables there. The public dashboard URL can then be shared with authorized staff.
