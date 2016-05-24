from distutils.core import setup

setup(
    name='esdeploy',
    version='0.0.1',
    packages=['lib'],
    install_requires=['argparse>=1.2.1',
                      'certifi>=2016.02.28',
                      'click>=6.6',
                      'elasticsearch>=2.3.0',
                      'nose>=1.3.7',
                      'sh>=1.11'],
    url='https://github.com/vedit/esdeploy',
    license='MIT',
    author='vedit',
    author_email='firatarig@gmail.com',
    description='Elasticsearch Index Deployment Workflow Tool',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='elasticsearch deployment workflow'
)
