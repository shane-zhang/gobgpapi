from __future__ import absolute_import
from __future__ import print_function
import connexion


import subprocess

def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        sorted list of people
    """
    # Create the list of people from our data
    rst = subprocess.check_output("screen -d -S pinger -m bash -c 'sudo python /home/vagrant/gobgpapi/pager.py /home/vagrant/gobgpapi/ping_list.txt'", shell= True)
    rst = subprocess.check_output("screen -ls", shell = True)
    print (rst)

    return rst
def create():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        sorted list of people
    """
    upload_file = connexion.request.files['upload_file']
    upload_file.save("ping_list.txt")
    print (upload_file)
    return 0
def delete():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        sorted list of people
    """
    rst = subprocess.check_output("screen -X -S pinger quit", shell= True)
    rst += subprocess.check_output("screen -ls", shell = True)
    return rst
