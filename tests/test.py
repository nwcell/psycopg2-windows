import sys
from pprint import pprint
try:
    import psycopg2
    pprint('Success: Python %s' % sys.version)
except ImportError:
    pprint('Failure: Python %s' % sys.version)
