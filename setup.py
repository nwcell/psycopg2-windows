from distutils.core import setup

setup(
    name='psycopg2',
    version='2.5.2',
    summary='Python-PostgreSQL Database Adapter',
    author='Federico Di Gregorio',
    author_email='fog@initd.org',
    description='Agnostic and easy to use ajax library for django',
    url='http://initd.org/psycopg',
    license='GPL with exceptions or ZPL',
    package_data={'dajaxice': ['templates/dajaxice/*']},
    long_description=("psycopg2 is a PostgreSQL database adapter for the Python programming "
                      "language.  psycopg2 was written with the aim of being very small and fast, "
                      "and stable as a rock. "
                       ""
                      "psycopg2 is different from the other database adapter because it was "
                      "designed for heavily multi-threaded applications that create and destroy "
                      "lots of cursors and make a conspicuous number of concurrent INSERTs or "
                      "UPDATEs. psycopg2 also provide full asynchronous operations and support "
                      "for coroutine libraries"),
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                 'License :: OSI Approved :: Zope Public License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.5',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.1',
                 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: C',
                 'Programming Language :: SQL',
                 'Topic :: Database',
                 'Topic :: Database :: Front-Ends',
                 'Topic :: Software Development',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: Unix']
)
