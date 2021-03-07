from datetime import datetime

def print_error(location,ex):
    print("\n>>>>>>>>>>>>>>>>>Oops!<<<<<<<<<<<<<<<<<\n",
                      'location: ',location ,'\n',
                      "class:",ex.__class__, "\n",
                      "Error:",ex, "\n","time:",datetime.now(), "\n",)