from ocs.ocs_client import OCSClient
client = OCSClient('satcouplingoptics')



#client.enable_axis(axis='E')

#client.jog_axis(axis='E', speed=20000.0)
#client.begin_axis_motion(axis='E')


#client.set_amp_currentloop_gain(axis='E',  val=0.0)
#client.set_torque_limit(axis='E', val=2.0)
#client.disable_axis(axis='E')
#client.disable_axis(axis='F')
#client.set_amp_gain(axis='E', val=0)
#client.set_off_on_error(axis='E', errtype=1)
#client.set_motortype(axis='E', motortype=1)
#time.sleep(1)
#client.acq.start()



#print('starting acq')
#client.acq.start()
response = client.acq.status()
print(response.session.get('data'))
