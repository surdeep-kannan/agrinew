import ee
import json
import os

PROJECT_ID = "premium-origin-469307-t0"

# Load service account JSON from Railway variable
service_json = os.getenv("SERVICE_ACCOUNT_JSON")

# Convert JSON string → Python dict
service_account_info = json.loads(service_json)

# Authenticate using service account
credentials = ee.ServiceAccountCredentials(
    email=service_account_info["client_email"],
    key_data=service_json
)

ee.Initialize(credentials, project=PROJECT_ID)
print("Earth Engine initialized on Railway!")
