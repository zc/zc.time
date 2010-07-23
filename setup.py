from setuptools import setup, find_packages

setup(
    name="zc.time",
    description="Hook for datetime for testing",
    version="0.3",
    license="ZVSL 1.0",
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    package_dir={'': 'src'},
    namespace_packages=['zc'],
    install_requires=[
        'pytz',
        'setuptools',
        ],
    )
