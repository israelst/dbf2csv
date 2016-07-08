from setuptools import setup

setup(name='dbf2csv',
        version='0.1',
        description='A straightforward lib to convert dbf files into csv',
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
        packages=['dbf2csv'],
        include_package_data=True,
        zip_safe=False)
