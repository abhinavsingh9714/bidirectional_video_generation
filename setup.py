from setuptools import setup, find_packages

# Load requirements from requirements.txt
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="video_bidi_gen",
    version="0.1",
    packages=find_packages(),
    install_requires=requirements,
)
