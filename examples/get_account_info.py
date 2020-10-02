from tronpy import Tron
from tronpy.exceptions import AddressNotFound
from pprint import pprint

client = Tron()

def get_account_info(address):
    try:
        info=client.get_account(address)
        return info
    except AddressNotFound:
        return 'Adress not found..!'


pprint(get_account_info('<address>'))
