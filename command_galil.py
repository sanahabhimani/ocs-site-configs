import time
from ocs.ocs_client import OCSClient
client = OCSClient('satcouplingoptics')


# to get/set motor type
print(client.get_motor_type(axis='F'))
print(client.get_motor_type(axis='E'))

client.set_motor_type(axis='F', motortype=1)


## to get/set off on error
client.get_off_on_error(axis='F')
client.set_off_on_error(axis='F', errtype=1)



## to get/set amp_gain
client.get_amp_gain(axis='E')
client.set_amp_gain(axis='E', val=0)


## to get/set torquelimit
client.set_torque_limit(axis='E', val=2.0)
print(client.get_torque_limit(axis='E'))



## get/set amp current loop gain
client.set_amp_currentloop_gain(axis='E',  val=0)
client.get_amp_currentloop_gain(axis='E')


# set gearing
client.set_gearing(order=',,,,,E;')
time.sleep(1)
client.set_gearing_ratio(order=',,,,,1;')

print(client.get_gearing_ratio(axis='E'))
print(client.get_gearing_ratio(axis='F'))

# get/set motor state, setting motor state means enabling/disabling motor
print(client.get_motor_state(axis='E'))
print(client.get_motor_state(axis='F'))

client.set_motor_state(axis='E', state='enable')
client.set_motor_state(axis='F', state='enable')



## to use input_configfile to initialize all settings notes in the config.yaml file
client.input_configfile(configfile='newconfig_EF.yaml')


## to jog axis and begin motion
client.set_jog_speed(axis='E', speed=8000.0)
client.begin_axis_motion(axis='E')


## set relative position, speed, or set absolute position
client.set_relative_position(axis='E', distance=2000.0, movetype='encoder') # 'linear', 'angular', or 'encoder'
client.set_speed(axis='E', speed=8000) # only defined in counts/sec
client.set_absolute_position(axis='E', position=25000, movetype='encoder') # 'linear', 'angular', or 'encoder'

## for homing once motor reaches limit switch 
client.define_position(axis='F', val=0)


## to stop motion
client.stop_axis_motion(axis='E')

## to set dwell times
client.set_dwell_times(t_first=1000, t_second=1500)

#print('starting acq')
#client.acq.start()
#response = client.acq.status()
#print(response.session.get('data'))
