# poc_inform
Proof of concept inform decoding and sniffing

**THIS REPO IS JUST A BRAINDUMP AND WILL LIKELY NOT BE UPDATED AS I TRANSFER THE CODE TO A MORE COMPLETE
LOCATION.**

## setup

```
virtualenv -p python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
python ./inform_sniffer.py

```

On the device you will need to repoint to this sniffer which will proxy the inform to the real controller.

```
mca-ctrl -t connect -s "<http://THISADDRESS:18080/inform>"
# To revert
mca-ctrl -t connect -s "<http://CONTROLLER:8080/inform>"
```

