from setuptools import setup, find_packages

setup(
    name='code_duck',
    version='0.1.0',
    description="This is an OpenAI-powered Python code analysis tool for reviewing code and making suggestions. It traverses a specified directory, conducting detailed analyses of functions and classes, and evaluates their adherence to SOLID principles and Pythonic style. ",
    author='Haruki',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'openai',
        'tqdm'
    ],
    entry_points={
        'console_scripts': [
            'code-duck=code_duck.analyzer:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: MIT',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.7',
)
