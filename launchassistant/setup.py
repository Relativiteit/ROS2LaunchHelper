from setuptools import setup

setup(
    name='param',
    version='0.1.0',
    py_modules=['param'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'param = param:method_collection',
        ],

    },
    
)