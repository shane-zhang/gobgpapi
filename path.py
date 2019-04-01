from __future__ import absolute_import
from __future__ import print_function


from datetime import datetime
import subprocess


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}




def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        sorted list of people
    """
    # Create the list of people from our data
    rst = subprocess.check_output("gobgp g r", shell= True)

    return rst
def create(str_para):
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        sorted list of people
    """
    print (str_para)
    rst = subprocess.check_output("gobgp global rib add "+ str_para["para"], shell= True)
    return rst
def delete(str_para):
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        sorted list of people
    """
    print (str_para)
    rst = subprocess.check_output("gobgp global rib del "+ str_para["para"], shell= True)
    return rst
