from requests import request
from enum import Enum
from etl.extract.event_class import Event

# Helper Classes

class Division(Enum):
    open = "H"
    pro = "HPRO"
    elite = "HE"
    doubles = "HD"
    relay = "HMR"
    goruck = "HG"
    goruck_doubles = "HDG"
    

class Gender(Enum):
    male = "M"
    female = "W"
    

# Helper Functions

def get_html(url: str):
    cookie_retrieval = request("GET", url)
    cookie = cookie_retrieval.request.headers.get("Cookie")
    response = request("GET", url, headers={"Cookie": cookie})
    return response.text


def removeprefix(x: str, prefix: str):
    if x.startswith(prefix):
        return x[len(prefix):]
    return x


def extract_event(event: Event, save_dir: str = "/kaggle/working"):
    hyrox_event = event.value.copy()
    hyrox_event.get_info()
    hyrox_event.save(directory=save_dir)
    

extract_event(Event.s6_losangeles2023)
