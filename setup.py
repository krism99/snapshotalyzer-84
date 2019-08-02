from setuptools import setup
setup(
    name='snapshotalyzer-84',
    version='0.1',
    author="Rbin",
    author_email="robin@acloud.guru",
    description="Tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/krism99/snapshotalyzer-84",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
    [console_scripts]
    shotty=shotty.shotty:cli
    ''',
)