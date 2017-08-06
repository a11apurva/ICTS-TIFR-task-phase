import requests
import pickle
import _thread
import time

api_key="ENTER API KEY"

i=0
start=1
end=10000

def get_db(id):
    global i
    global end
    while 1:
        try:
            r = requests.get('https://api.themoviedb.org/3/movie/' + str(id) + '?api_key='+ api_key )
            if 'status_code' not in r.json():
                with open('moviedb' + str(id) +'.pickle', 'wb') as handle:
                    pickle.dump(r, handle, protocol=pickle.HIGHEST_PROTOCOL)
                i=i+1
                if(i==100):
                    print("downloaded till ID: "+str(id))
                    i=0
                    if(id>end):
                        print("***done***")
                        break
            id = id+1
            
            				
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print("Error on id " + str(id) + ", retrying...")
            id = id+1

get_db(start)
