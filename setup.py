from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='dbf2csv',
        version='0.1',
        description='A straightforward lib to convert dbf files into csv',
        long_description=readme(),
        url='http://github.com/israelst/dbf2csv',
        author='Israel Teixeira',
        author_email='israelst@gmail.com',
        keywords='utility dbf convert csv ',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Programming Language :: Python',
            'Topic :: Database',
            'Topic :: Utilities',
            ],
        license='GPLv3+',
        install_requires=[
            'dbfread',
        ],
        packages=['dbf2csv'],
        scripts=['bin/dbf2csv'],
        include_package_data=True,
        zip_safe=False)
