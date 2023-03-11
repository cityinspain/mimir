import tomli
import pandas as pd
import unicodedata

with open('config.toml', 'rb') as f:
    CONFIG = tomli.load(f)

    REGISTER_PARSE_CONFIG = CONFIG['register']['parse']

    COLUMN_CONFIG = REGISTER_PARSE_CONFIG['columns']

    INT_THEN_STRING_COLUMNS = COLUMN_CONFIG['to_int_then_string']
    INT64_COLUMNS = COLUMN_CONFIG['to_int64']
    STRING_KEY_COLUMNS = COLUMN_CONFIG['string_key']
    DISCARD_COLUMNS = COLUMN_CONFIG['discard']
    RENAME = COLUMN_CONFIG['rename']


def fix_floated_strint(strint):

    return int(float(strint))


def fix_floated_strint_cols(row):

    for col in INT_THEN_STRING_COLUMNS:
        if row[col] != '':
            row[col] = fix_floated_strint(row[col])

    return row


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')
