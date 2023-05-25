from setuptools import setup

setup(
    name='demo-dnd-server',
    version='0.0.0',
    url='https://github.com/flox-examples/dnd-demo-server.git',
    author='Zach Mitchell',
    author_email='zach@floxdev.com',
    description='A server that queries a D&D 5th Edition API',   
    install_requires=[],
        entry_points={
        'console_scripts': [
            'demo-dnd-server = server:main',
        ]
    },
    py_modules=['server']
)