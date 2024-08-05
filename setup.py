from setuptools import setup, find_packages

setup(
    name='cli_py',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'git+https://github.com/Mythical-Github/python_logging.git',
    ],
    include_package_data=True,
    package_data={
        '': ['cli.json.example'],
    },
    description='A Python module with various cli functionality',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Mythical-Github/cli_py',
    author='Mythical',
    author_email='mythicaldata.com',
    license='GPL3',
)
