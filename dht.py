import json
import Adafruit_DHT
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

sensor=Adafruit_DHT.DHT11
 
gpio=17
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

data ={ "sensor ":{

            "Temp":{
                "value": temperature     
            },
            "humidity":{
                "value": humidity    
                }
}
}            



 
if humidity is not None and temperature is not None:

    out_file = io.open('data.json', 'w', encoding='utf8') 
    str_ = json.dumps(data,
                    indent=4, sort_keys=True,
                    separators=(',', ': '), ensure_ascii=False)
    out_file.write(to_unicode(str_))
else:
     print('Failed to get reading. Try again!')


