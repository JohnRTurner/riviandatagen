#from random import randrange, choice, uniform, getrandbits
import time

from faker import Faker
from datetime import datetime
import numpy as np



#Define a list
type=['type_a','type_b','type_c', 'type_d', 'type_e' ]
sub_type=['sub_type_100', 'sub_type_200','sub_type_300','sub_type_400','sub_type_500']
source_type=['Car','Charger','R1T','R1S','Commercial Van']
tenant=['Rivian','Corporate','Fleet','Other']
realColumns=['fleet','raw_stream_ref','_subtype','_type','_updated','_seq','car_ownership_id','temperature_IGBT_A','motor_temperature','temperature_IGBT_C','temperature_IGBT_B','_id','updated','_source_type','tenant','std_stream_ref']
 
def gen_event(thread, fake):
 return {
   "fleet": fake.pystr(32,32) + '/' + fake.pystr(32,32) + '/' + fake.pystr(32,32),
   'std_stream_ref': {
       'partition': fake.random_int(1,32),
       'offset': fake.random_number(digits=9),
       'timestamp': datetime.timestamp(datetime.now())
    },
   'raw_stream_ref': {
       'partition': fake.random_int(1, 32),
       'offset': fake.random_number(digits=9),
       'timestamp': datetime.timestamp(datetime.now())
    },
   "_subtype": np.random.choice(sub_type, p=(0.1, 0.1, 0.2, 0.2, 0.4)), #p(robability) has to add up to value of 1
   "_type": np.random.choice(type),
   '_event_timing': fake.random_int(1,10),
   '_updated': datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%f'),
   '_seq': fake.random_number(digits=6),
   'car_ownership_id': fake.random_number(digits=8),
   'realColumns': realColumns,
   'motor_temperature': fake.pyfloat(2,2,True,50,75), #pyfloat(left_digits=None, right_digits=None, positive=False, min_value=None, max_value=None)
   'temperature_IGBT_A': fake.pyfloat(2,2,True,50,75),
   'temperature_IGBT_B': fake.pyfloat(2,2,True,50,75),
   'temperature_IGBT_C': fake.pyfloat(2,2,True,50,75),
   '_id': ((time.clock_gettime_ns(time.CLOCK_MONOTONIC_RAW) % 100000000000) * 100) + thread,
   'updated': 'null',
   '_source_type': np.random.choice(source_type),
   'tenant': np.random.choice(tenant)
 }



def gen_events(batch_size, thread):
  Faker.seed()
  fake = Faker()
  return [gen_event(thread, fake) for _ in range(1, (batch_size + 1))]
