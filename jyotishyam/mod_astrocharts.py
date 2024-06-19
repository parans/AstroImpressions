from __future__ import annotations
from pydantic import BaseModel, Field

import mod_astrodata as data
import json


class D1Chart:
      def __init__(self, dictionary=None):
          
          if dictionary != None :
               for k, v in dictionary.items():
                    setattr(self, k, v)
               return
           
          sun = dict(data.lagna_sun)
          moon = dict(data.lagna_moon)
          mars = dict(data.lagna_mars)
          mercury = dict(data.lagna_mercury)
          jupiter = dict(data.lagna_jupiter)
          venus = dict(data.lagna_venus)
          saturn = dict(data.lagna_saturn)
          rahu = dict(data.lagna_rahu)
          ketu = dict(data.lagna_ketu)

          self.planets = dict(data.lagna_planets)
          self.planets["Sun"] = sun
          self.planets["Moon"] = moon
          self.planets["Mars"] = mars
          self.planets["Mercury"] = mercury
          self.planets["Jupiter"] = jupiter
          self.planets["Venus"] = venus
          self.planets["Saturn"] = saturn
          self.planets["Rahu"] = rahu
          self.planets["Ketu"] = ketu

          self.ascendant = dict(data.lagna_ascendant)

          self.houses = []
          self.classifications = {}
          self.classifications["benefics"] = []
          self.classifications["malefics"] = []
          self.classifications["neutral"] = []
          self.classifications["kendra"] = []
          self.classifications["trikona"] = []
          self.classifications["trik"] = []
          self.classifications["upachaya"] = []
          self.classifications["dharma"] = []
          self.classifications["artha"] = []
          self.classifications["kama"] = []
          self.classifications["moksha"] = []   

          self.symbol = "D1"
          self.name = "Lagna"    

class VedicCharts:
      def __init__(self):
           self.D1 = D1Chart()
           self.user_details = {"maasa" :"",
                            "vaara" : "",
                            "tithi" : "",
                            "karana" : "",
                            "nakshatra" : "",
                            "yoga" : "",
                            "rashi" : ""}
      
      def to_dict(self):
           return json.loads(json.dumps(self, default=lambda o: o.__dict__))


class DateOfBirth(BaseModel):
    year: str
    month: str
    day: str


class TimeOfBirth(BaseModel):
    hour: str
    min: str
    sec: str


class PlaceOfBirth(BaseModel):
    name: str
    lon: str
    lat: str
    timezone: str


class BirthDetails(BaseModel):
    date_of_birth: DateOfBirth = Field(..., alias='DateOfBirth')
    time_of_birth: TimeOfBirth = Field(..., alias='TimeOfBirth')
    place_of_birth: PlaceOfBirth = Field(..., alias='PlaceOfBirth')
    name: str = Field(..., alias='Name')
    gender: str = Field(..., alias='Gender')
    comments: str = Field(..., alias='Comments')