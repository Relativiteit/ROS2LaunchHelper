from setuptools import find_packages, setup

package_name = 'python'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='chevre',
    maintainer_email='chevre@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "yamazaki_publisher = python.yamazaki_publisher:main",
            "yamazaki_subscriber = python.yamazaki_subscriber:main",
            "beppi_pubsub = python.beppi_pubsub:main",


        ],
    },
)
