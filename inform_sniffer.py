import base64
import json
import struct

import zlib
from Crypto.Cipher import AES
from binascii import a2b_hex
from flask import Flask, request, Response

from Inform import *

from time import time

import requests

app = Flask(__name__)

real_url = 'http://192.168.111.20:8080/inform'



#foo = packet_decode(a2b_hex("ba86f2bbe107c7c57eb5f2690775c712"), data)

@app.route("/inform", methods=['POST'])
def inform():
    global dummy
    data = request.get_data()

    inform = Packet(from_packet=data, key='1C6592EF70601F95D2B24A3A0B420B62')
    print("FROM DEVICE: ", inform)
    #print(inform.payload_decoded)
    foo = json.loads(inform.payload_decoded)
    json.dump(foo,open('sniff-{}.json'.format(time()),'wt'),indent=4)

    out = requests.post(real_url, data=data)
    raw_reply = out.content
    #print(type(raw_reply))

    reply = Packet(from_packet=raw_reply, key='1C6592EF70601F95D2B24A3A0B420B62')

    print("REPLY: ", reply.payload_decoded)

    return raw_reply



#mca-ctrl -t connect -s "http://10.0.8.2:8080/inform" -k "A09E428C482EB53C7731C224295CD9D3"



app.run(debug=True, port=18080, host='0.0.0.0')
