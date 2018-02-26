import sys

from setuptools import find_packages, setup

setup(
    name="pynome",
    description="a litle help when you need to find someone to complete you",
    version="0.0.1",
    author="Yohann",
    author_email="yohann@rebattu.fr",
    packages=find_packages(),
    package_data={
        'data': ['alembic/sql/*.sql', 'alembic.ini', 'alembic-*.ini']
    },
    entry_points={'console_scripts': [
        'pynome=pynome.__main__:main',
    ]},
    install_requires=[
        'flask', 'flask_sqlalchemy', 'mandrill>=1.0.57', 'alembic', 'flask_login',
        'wtforms_alchemy'
    ])
