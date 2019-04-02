from __future__ import absolute_import
from __future__ import print_function


import subprocess

def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        sorted list of people
    """
    # Create the list of people from our data
    rst = subprocess.check_output("gobgp neighbor", shell= True)
    print (rst)

    return rst
def create(str_para):
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        sorted list of people
    """
    print (str_para)
    rst = subprocess.check_output("gobgp neighbor add "+ str_para["para"], shell= True)
    return rst
def delete(str_para):
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        sorted list of people
    """
    print (str_para)
    rst = subprocess.check_output("gobgp neighbor del "+ str_para["para"], shell= True)
    return rst
