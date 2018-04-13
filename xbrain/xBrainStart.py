from subprocess import call
import intern
from intern.remote.dvid import DVIDRemote

# #Starts Dockers
# call(["docker-compose", "up"])

#DVID Data fetch:
dvid = DVIDRemote({
	"protocol": "http",
	"host": "localhost:8000",
	})

#Creating Project, and chanel to store boxed data in
proj = dvid.create_project('Xbrain_Proj1','Data upload test')
chan_setup = dvid.ChannelResource(proj, "MaskedImg1")


#Uploads Data
call(["docker-compose", "exec", "dvid", "dvid", "node", proj, "MaskedImg1", "load", "0" + "," + "0" + "," + "390", "dataLoad/*.tif"])
print("The dvid instance has your requested data sample.")
