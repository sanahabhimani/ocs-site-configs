import time
from ocs.ocs_client import OCSClient


client = OCSClient('satcouplingoptics')
client.acq.start()
client.acq.stop()
#print('waiting 5 seconds')
#time.sleep(5)

axis ='B'
response = client.release_axis_brake(axis='B')
# Will be True or False depending on successful completion
if response.session['success']:
    print('Task completed successfully')
else:
    print('Task did not complete successfully')

