#!/var/log/nagios/.pythonbrew/venvs/Python-2.7.10/pyez/bin/python
import sys
from jnpr.junos import Device

host = sys.argv[1]
int = sys.argv[2]
ret = 0
dev = Device(host=host, user='tools')

dev.open()
opt = dev.rpc.get_interface_optics_diagnostics_information(interface_name=int)
des = dev.rpc.get_interface_information(interface_name=int)
dev.close()

if opt.findtext('.//optic-diagnostics-not-available'):
	print "Not supported"
	sys.exit(ret)

description = des.findtext('.//description').strip()
try:
	input_dbm = float( opt.findtext('.//rx-signal-avg-optical-power-dbm').strip() )
except AttributeError:
	input_dbm = float( opt.findtext('.//laser-rx-optical-power-dbm').strip() )
output_dbm = float( opt.findtext('.//laser-output-power-dbm').strip() )
low_alarm = float( opt.findtext('.//laser-rx-power-low-alarm-threshold-dbm').strip() )
high_alarm = float( opt.findtext('.//laser-rx-power-high-alarm-threshold-dbm').strip() )
temp = opt.findtext('.//module-temperature').strip()
temp_c = float( temp[0:2] )

output = "(%s) Input(dbm): %0.2f, Output(dbm): %0.2f, Temp: %s |input=%0.2fdbm output=%0.2fdbm temp=%0.0fC" % (description, input_dbm, output_dbm, temp, input_dbm, output_dbm, temp_c)

if low_alarm < input_dbm < high_alarm:
	print output
else:
	ret = 2
	print output

sys.exit(ret)
