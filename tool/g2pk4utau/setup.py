import setuptools

REQUIRED_PACKAGES = [
    "jamo",
    "regex",
    "g2pk",
]

setuptools.setup(
    name="g2pk4utau",
    version="0.0.3",
    author="Cardroid",
    author_email="carbonsindh@gmail.com",
    description="g2pk4utau: g2p module for Korean utau",
    install_requires=REQUIRED_PACKAGES,
    license="MIT",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
)
