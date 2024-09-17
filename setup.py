from setuptools import setup, find_packages

setup(
    name="mobile_automation_project",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "appium==2.4.0",
        "behave==1.2.7",
        "selenium==4.1.0",
    ],
)
