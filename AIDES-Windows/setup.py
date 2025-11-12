from setuptools import setup, find_packages
setup(
    name='AIDES-Windows',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'psutil', 'pyyaml', 'rich'
    ],
    entry_points={
        'console_scripts': [
            'aides-windows = aides.main:cli_entry'
        ]
    }
)
