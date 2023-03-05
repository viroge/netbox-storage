from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='netbox-storage-plugin',
    version='0.6.2',
    description='NetBox storage plugin',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    author='Gabor Somogyvari',
    url='https://github.com/viroge/netbox-storage',
    keywords=['netbox', 'netbox-plugin'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 4 - Beta',
    ]
)
