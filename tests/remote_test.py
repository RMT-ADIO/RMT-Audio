from rmt_audio.remote import remote
import asyncio
from bleak import BleakClient

def test_first():
    v = remote(1,2,3)
    assert v is not None


