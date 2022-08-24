#from random import randrange, choice, uniform, getrandbits
import time

from faker import Faker
from datetime import datetime
import numpy as np

fake = Faker()

type=['Type A','Type B','Type C']
sub_type=['Sub Type 100', 'Sub Tupe 200','Sub Type 300']
source_type=['Car','Charger','R1T','R1S','Commercial Van']
tenant=['Rivian','Corporate','Fleet','Other']
# Specify probabilities of each category (must sum to 1.0)
weights = [0.6, 0.2, 0.1, 0.07, 0.03]

def gen_event(thread):
  return {
    "fleet": fake.pystr(32,32) + '/' + fake.pystr(32,32) + '/' + fake.pystr(32,32),
    "_type": np.random.choice(type),
    "_sub_type": np.random.choice(sub_type),
    '_event_timing': fake.random_int(1, 10),
    '_updated': datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%f'),
    '_seq': fake.random_number(digits=6),
    'car_ownershp_id': fake.random_number(digits=10),
    'motor_temperature': fake.random_int(50, 75),
    'temperatures': {
        'temperature_IGBTA': fake.random_int(50, 75),
        'temperature_IGBT_B': fake.random_int(50, 75),
        'temperature_IGBT_C': fake.random_int(50, 75)
     },
    '_id': ((time.clock_gettime_ns(time.CLOCK_MONOTONIC_RAW) % 100000000000) * 100) + thread,
    'updated': '',
    '_source_type': np.random.choice(source_type),
    'tenant': np.random.choice(tenant)
  }


def gen_events(batch_size, thread):
  return [gen_event(thread) for _ in range(1, (batch_size + 1))]
