
from setuptools import find_packages, setup

with open("security_scanner/README.md", "r") as f:
    long_description = f.read()

setup(
    name="security_scanner",
    version="0.1.4",
    description="Password/passphrase strength and health checker",
    package_dir={"": "security_scanner"},
    packages=find_packages(where="security_scanner"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheNewThinkTank/security-scanner",
    author="TheNewThinkTank",
    author_email="TheNewThinkTank@users.noreply.github.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    install_requires=["bson >= 0.5.10"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.11",
)
