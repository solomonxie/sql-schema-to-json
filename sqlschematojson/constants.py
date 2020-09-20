import re

DDL_TOKENS = ['CREATE']

KEYWORDS = [
    'TABLE',
    'PRIMARY',
    'KEY',
    'NOT',
    'NULL',
]

CTYPES_SNOWFLAKE = [
    'NUMBER',
    'FLOAT',
    'ARRAY',
    'DATE',
    'TIME',
    'TIMESTAMP',
]

DEFAULT_VALUES_SNOWFLAKE = [
    'not null',
    'nullable',
]

REGX_CREATE = re.compile(
    r'create\s+table\s+(?P<fulltablename>[^ ]+)\s+\((?P<columns>[^;]+)+\s+\);'
)
REGX_COLUMN = re.compile(
    r'(?P<colname>[^ ,]+)\s+(?P<ctype>[^ ,]+)\s*(?P<default>[^,]+)?'
)
REGX_PK = re.compile(
    r'primary\s+key\s+\((?P<pkname>[^()]+)\)'
)
