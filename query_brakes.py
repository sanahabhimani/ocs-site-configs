import time
from ocs.ocs_client import OCSClient


client = OCSClient('satcouplingoptics')
client.acq.start()
client.acq.stop()
#print('waiting 5 seconds')
#time.sleep(5)


response = client.get_brake_status()
# Will be True or False depending on successful completion
if response.session['success']:
    print('Task completed successfully')
else:
    print('Task did not complete successfully')

