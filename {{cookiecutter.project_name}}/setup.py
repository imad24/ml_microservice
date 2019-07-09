from setuptools import find_packages, setup

setup(
    name='{{cookiecutter.package_name}}',
    packages=find_packages(),
    version=version,
    description='{{cookiecutter.description}}',
    author='{{cookiecutter.author}}',
    license='',
    python_requires='>=3',
    install_requires=['numpy', 'pandas','scikit-learn'],
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Data Science :: Data tools',
    'Programming Language :: Python :: 3.6',
    ],
)
