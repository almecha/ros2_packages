from setuptools import find_packages, setup

package_name = 'lab01_pkg'

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
    maintainer='nukharetrd',
    maintainer_email='nukharetrd@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_publisher_node = lab01_pkg.my_controller_node:main",
            "test_subscriber_node = lab01_pkg.my_localization_node:main",
            "test_reset_node = lab01_pkg.my_reset_node:main",
            "test_reset_controller_node = lab01_pkg.my_reset_controller_node:main",
            "test_reset_localization_node = lab01_pkg.my_reset_localization_node:main"

        ],
    },
)
