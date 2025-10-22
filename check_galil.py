from ocs.ocs_client import OCSClient
client = OCSClient('satcouplingoptics')
#client.get_motor_type(axis='F')

#client.set_motor_type(axis='F', motortype=1)
#client.get_off_on_error(axis='F')
#client.set_off_on_error(axis='F', errtype=1)

#client.get_amp_gain(axis='E')
#client.set_amp_gain(axis='E', val=0)
#client.get_amp_gain(axis='E')


#client.get_amp_gain(axis='F')
#client.set_amp_gain(axis='F', val=0)
#client.get_amp_gain(axis='F')





#client.set_torque_limit(axis='F', val=2.0)

#client.set_torque_limit(axis='F', val=2.0)



#client.get_amp_currentloop_gain(axis='E')
#client.set_amp_currentloop_gain(axis='E',  val=0)
#client.get_amp_currentloop_gain(axis='E')


#client.get_amp_currentloop_gain(axis='F')
#client.set_amp_currentloop_gain(axis='F',  val=0)
#client.get_amp_currentloop_gain(axis='F')


#client.set_gearing(order=',,,,,E;')
#client.set_gearing_ratio(order=',,,,,1;')

#client.get_gearing_ratio(axis='E')
#client.get_gearing_ratio(axis='F')

# now enable the motor
#client.get_motor_state(axis='F')
#client.set_motor_state(axis='F', state='enable')
#client.get_motor_state(axis='F')




client.jog_axis(axis='E', speed=8000.0)
client.begin_axis_motion(axis='E')





#print('starting acq')
#client.acq.start()
response = client.acq.status()
print(response.session.get('data'))
