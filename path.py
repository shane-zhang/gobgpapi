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

import grpc
from google.protobuf.any_pb2 import Any

import gobgp_pb2
import gobgp_pb2_grpc
import attribute_pb2

_TIMEOUT_SECONDS = 1000


def AddPath():
    channel = grpc.insecure_channel('localhost:50051')
    stub = gobgp_pb2_grpc.GobgpApiStub(channel)

    nlri = Any()
    nlri.Pack(attribute_pb2.IPAddressPrefix(
        prefix_len=24,
        prefix="10.192.1.0",
    ))
    origin = Any()
    origin.Pack(attribute_pb2.OriginAttribute(
        origin=2,  # INCOMPLETE
    ))
    as_segment = attribute_pb2.AsSegment(
        # type=2,  # "type" causes syntax error
        numbers=[65000],
    )
    as_segment.type = 2  # SEQ
    as_path = Any()
    as_path.Pack(attribute_pb2.AsPathAttribute(
        segments=[as_segment],
    ))
    next_hop = Any()
    next_hop.Pack(attribute_pb2.NextHopAttribute(
        next_hop="10.0.0.20",
    ))
    attributes = [origin, as_path, next_hop]

    stub.AddPath(
        gobgp_pb2.AddPathRequest(
            table_type=gobgp_pb2.GLOBAL,
            path=gobgp_pb2.Path(
                nlri=nlri,
                pattrs=attributes,
                family=gobgp_pb2.Family(afi=gobgp_pb2.Family.AFI_IP, safi=gobgp_pb2.Family.SAFI_UNICAST),
            )
        ),
        _TIMEOUT_SECONDS,
    )

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

