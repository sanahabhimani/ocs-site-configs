from ocs.ocs_client import OCSClient
client = OCSClient('satcouplingoptics')
client.acq.stop()
response = client.acq.status()
print(response.session)
