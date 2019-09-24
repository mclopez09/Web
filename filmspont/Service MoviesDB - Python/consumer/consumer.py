import json
import datetime
import http.client
from time import time

########################################################################################################################
##################################################### ENVIRONMENTS #####################################################
########################################################################################################################

#local
#conn = http.client.HTTPConnection("localhost:5008")

#container
conn = http.client.HTTPConnection("localhost:5008")

########################################################################################################################
######################################################## ROLES  #########################################################
########################################################################################################################

conn.request("GET", "/rol?page=0", headers={'Content-type': 'application/json'})

#conn.request("GET", "/rol?page=0&name=%director%", headers={'Content-type': 'application/json'})


#conn.request("GET", "/rol/12", headers={'Content-type': 'application/json'})

#create_rol_post = {
#     'name': 'coWriter32'
# }
#json_data_post = json.dumps(create_rol_post)
#conn.request("POST", "/rol", json_data_post, headers={'Content-type': 'application/json'})

#create_rol_post = {
#     'name': 'coWriter8' 
#}
#json_data_post = json.dumps(create_rol_post)
#conn.request("PUT", "/rol/12", json_data_post, headers={'Content-type': 'application/json'})

#conn.request("DELETE", "/rol/9", headers={'Content-type': 'application/json'})

########################################################################################################################
######################################################## MOVIES #########################################################
########################################################################################################################


#create_movie_post = {
#     'name': 'Harry Potter y la piedra filosofal',
#     'des': 'Niño busca piedra',
#     'year': '2001'
# }
#json_data_post = json.dumps(create_movie_post)
#conn.request("POST", "/movie", json_data_post, headers={'Content-type': 'application/json'})

#conn.request("GET", "/movie?page=0", headers={'Content-type': 'application/json'})




start = datetime.datetime.now()
res = conn.getresponse()
end = datetime.datetime.now()
	
data = res.read()

elapsed = end - start

print(data.decode("utf-8"))
print("\"" + str(res.status) + "\"")
print("\"" + str(res.reason) + "\"")
print("\"elapsed seconds: " + str(elapsed) + "\"")

