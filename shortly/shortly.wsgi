import sys
import os
sys.path.append(os.getcwd())

# For test
#from testapp import application

# Shortly
from shortly import create_app
application = create_app()