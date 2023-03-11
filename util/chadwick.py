import pandas as pd
import datetime

import tomli


with open('config.toml', 'rb') as f:
    CONFIG = tomli.load(f)

    REGISTER_PARSE_CONFIG = CONFIG['register']['parse']

    COLUMN_CONFIG = REGISTER_PARSE_CONFIG['columns']

    INT_THEN_STRING_COLUMNS = COLUMN_CONFIG['to_int_then_string']
    INT64_COLUMNS = COLUMN_CONFIG['to_int64']
    STRING_KEY_COLUMNS = COLUMN_CONFIG['string_key']
    DISCARD_COLUMNS = COLUMN_CONFIG['discard']
    RENAME = COLUMN_CONFIG['rename']


def create_birth_date(row):
    birth_year = row['birth_year']
    birth_month = row['birth_month']
    birth_day = row['birth_day']

    if pd.isna(birth_year) or pd.isna(birth_month) or pd.isna(birth_day):
        return None
    else:
        return datetime.date(birth_year, birth_month, birth_day)


def set_active(row):
    if row['pro_played_last'] == datetime.date.today().year:
        return True
    else:
        return False


def combine_name(row):
    first = row['name_first']
    last = row['name_last']
    if pd.isna(first):
        return ""
    if pd.isna(last):
        return ""

    return first + ' ' + last


def process_register_df(df):

    df = df.drop(DISCARD_COLUMNS, axis=1)

    # remove players who never played pro ball
    if REGISTER_PARSE_CONFIG['drop_non_pro_players']:
        df = df[~df['pro_played_first'].isnull()]

    for column in INT_THEN_STRING_COLUMNS:
        df[column] = df[column].fillna(0)
        df[column] = df[column].astype(int)
        df[column] = df[column].astype(str)
        df[column] = df[column].replace('0', '')

    for column in STRING_KEY_COLUMNS:
        df[column] = df[column].fillna('')
        df[column] = df[column].astype(str)

    for column in INT64_COLUMNS:
        df[column] = df[column].astype('Int64')

    df['register_name'] = df.apply(combine_name, axis=1)
    df.drop(['name_first', 'name_last', 'name_given', 'name_suffix',
             'name_matrilineal', 'name_nick'], axis=1, inplace=True)

    # assign birth_date column, returning None if not all values are present
    # drop birth_month and birth_day either way - inaccurate data will be lost here
    df['birth_date'] = df.apply(create_birth_date, axis=1)
    df.drop(['birth_month', 'birth_day'], axis=1, inplace=True)

    # assign active column according to pro_played_last
    # TODO: fix this, it's inaccurate
    df['register_active'] = df.apply(set_active, axis=1)

    # rename columns in df according to rename dict
    df.rename(columns=RENAME, inplace=True)

    return df
