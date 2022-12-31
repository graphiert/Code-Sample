import os, shutil, subprocess
print("Initializing...")

"""
Make sure you have Git, Python (of course), and `python-pip` installed
Constants variables:
  GIT_TOKEN = https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
  REPO_URL = Github repository, which is contains `requirements.txt`, `__init__.py` and `__main__.py`
  PACKAGE_FOLDER = Package folder name
"""

if GITHUB_TOKEN:
    TEMP_REPO = REPO_URL.split("https://")[1]
    UPSTREAM_REPO = f"https://{GITHUB_TOKEN}@{TEMP_REPO}"
else:
    UPSTREAM_REPO = REPO_URL
try:
    shutil.rmtree(f"{PACKAGE_FOLDER}/")
except Exception:
    pass
ready_to_exc = f"git clone {UPSTREAM_REPO} {PACKAGE_FOLDER} && "
ready_to_exc += f"pip3 install --no-cache-dir -U -r {PACKAGE_FOLDER}/requirements.txt"
print("Fetching the Latest updates and installing the requirements...")
subprocess.call(ready_to_exc, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
print("Fetched the updates and starting the bot...")
os.system(f"python3 -m {PACKAGE_FOLDER}")
