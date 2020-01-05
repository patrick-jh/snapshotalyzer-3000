from setup tools import setup

setup(
    name='snapshot',
    version='0.1',
    author="ASDF",
    author_email="email",
    description="List EC2 instances, their volumes, start and stop instances, take snapshots of their volumes",
    license="GPLv3+",
    packages=['shot'],
    url="mygit",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shot=shot.shot:cli
    '''
)
