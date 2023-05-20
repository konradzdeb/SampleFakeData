#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# generate_sample_df.py
# Created 2023-05-20 10:42
#
#

"""
Convenience script generating sample data using Faker and returning a
pandas data frame.
"""

import pandas as pd
from faker import Faker
import random

def create_sample_data(num_rows: int=5000, faker_seed: int=123) -> pd.DataFrame:
    fake = Faker()
    Faker.seed(seed=faker_seed)
    output = [{"name":fake.name(),
               "address":fake.address(),
               "name":fake.name(),
               "email":fake.email(),
               "address":fake.address(),
               "city":fake.city(),
               "phone": fake.phone_number(),
               "country":fake.country(),
               "credit_card_no":fake.credit_card_number(),
               "credit_card_expire": fake.credit_card_expire(),
               "date_time":fake.date_time(),
               "random_int":random.randint(0,num_rows)} for x in range(num_rows)]
    df = pd.DataFrame(output)
    return df
