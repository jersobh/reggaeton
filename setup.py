from setuptools import setup, find_packages

setup(
    name="reggaeton",
    version="0.1.0",
    author="jersobh",
    author_email="jersobh@gmail.com",
    description="Reggaeton is simple image comparison tool for detecting regressions in images.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jersobh/reggaeton",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "opencv-python",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'reggaeton=reggaeton_cli:main', 
        ],
    },
    python_requires='>=3.6',
)
