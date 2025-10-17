from ocs.ocs_client import OCSClient
client = OCSClient('satcouplingoptics')
client.acq.start()
response = client.acq.status()
print(response.session)
