"""
Example local settings that are specific to this particular instance of the project.

This can contain sensitive information (such as keys) and should not be shared with others.

HOW TO USE:

1. Make a copy of this file and rename it to `local_settings.py`.
2. In `local_settings.py`, fill in the values for the variables below.
3. Do NOT commit `local_settings.py` to version control
4. If you make any changes to `local_settings.py`, please update `local_settings.example.py` as well.
"""

from pathlib import Path

from google.oauth2 import service_account

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "testserver"]

# Create a SECRET_KEY.
# Online tools can help generate this for you, e.g. https://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = ""

# Google Cloud settings

GCP_PROJECT_ID = ""
GCP_ZONE = ""
GCP_CLUSTER = ""
GCP_SA_KEY = ""
GCP_CREDENTIALS = service_account.Credentials.from_service_account_file(
    Path.joinpath(BASE_DIR, GCP_SA_KEY)
)

# React settings
CORS_ORIGIN_WHITELIST = [""]
