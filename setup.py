#!/usr/bin/env python3
"""Home Assistant setup script."""
from datetime import datetime as dt

from setuptools import find_packages, setup

import homeassistant.const as hass_const

PROJECT_NAME = "Home Assistant"
PROJECT_PACKAGE_NAME = "homeassistant"
PROJECT_LICENSE = "Apache License 2.0"
PROJECT_AUTHOR = "The Home Assistant Authors"
PROJECT_COPYRIGHT = f" 2013-{dt.now().year}, {PROJECT_AUTHOR}"
PROJECT_URL = "https://www.home-assistant.io/"
PROJECT_EMAIL = "hello@home-assistant.io"

PROJECT_GITHUB_USERNAME = "home-assistant"
PROJECT_GITHUB_REPOSITORY = "core"

PYPI_URL = f"https://pypi.python.org/pypi/{PROJECT_PACKAGE_NAME}"
GITHUB_PATH = f"{PROJECT_GITHUB_USERNAME}/{PROJECT_GITHUB_REPOSITORY}"
GITHUB_URL = f"https://github.com/{GITHUB_PATH}"

DOWNLOAD_URL = f"{GITHUB_URL}/archive/{hass_const.__version__}.zip"
PROJECT_URLS = {
    "Bug Reports": f"{GITHUB_URL}/issues",
    "Dev Docs": "https://developers.home-assistant.io/",
    "Discord": "https://discordapp.com/invite/c5DvZ4e",
    "Forum": "https://community.home-assistant.io/",
}

PACKAGES = find_packages(exclude=["tests", "tests.*"])

REQUIRES = [
    "aiohttp==3.7.4.post0",
    "astral==2.2",
    "async_timeout==3.0.1",
    "attrs==21.2.0",
    "awesomeversion==21.8.1",
    'backports.zoneinfo;python_version<"3.9"',
    "bcrypt==3.1.7",
    "certifi>=2020.12.5",
    "ciso8601==2.1.3",
    "httpx==0.19.0",
    "jinja2==3.0.1",
    "PyJWT==2.1.0",
    # PyJWT has loose dependency. We want the latest one.
    "cryptography==3.4.8",
    "pip>=8.0.3,<20.3",
    "python-slugify==4.0.1",
    "pyyaml==5.4.1",
    "requests==2.25.1",
    "voluptuous==0.12.1",
    "voluptuous-serialize==2.4.0",
    "yarl==1.6.3",
]

MIN_PY_VERSION = ".".join(map(str, hass_const.REQUIRED_PYTHON_VER))

setup(
    name=PROJECT_PACKAGE_NAME,
    version=hass_const.__version__,
    url=PROJECT_URL,
    download_url=DOWNLOAD_URL,
    project_urls=PROJECT_URLS,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIRES,
    python_requires=f">={MIN_PY_VERSION}",
    test_suite="tests",
    entry_points={"console_scripts": ["hass = homeassistant.__main__:main"]},
)
