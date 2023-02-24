from setuptools import find_packages, setup

setup(
    name='netbox-storage',
    version='0.6.2',
    description='NetBox storage plugin',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    author='Gabor Somogyvari',
)
