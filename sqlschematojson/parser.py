from sqlschematojson import constants
from sample import sql_statements


def normalize_sql(sql):
    return ' '.join(sql.strip().split()).lower()


def parse(raw_sql):
    result = {}
    sql = normalize_sql(raw_sql)
    match = constants.REGX_CREATE.match(sql)
    table = match.groupdict() if match else None
    if not table:
        raise RuntimeError(f'Cannot interpret CREATE statement: {sql}')
    tablename = table['fulltablename']
    columns = normalize_sql(table['columns']).split(',')
    column_def = {}
    primary_key = None
    for c in columns:
        match = constants.REGX_COLUMN.match(normalize_sql(c))
        col = match.groupdict() if match else None
        if not col:
            __import__('pudb').set_trace()
            raise RuntimeError(f'Cannot interpret Column statement: {c}')
        if col['colname'] == 'primary':
            primary_key = col['default']
            continue
        column_def[col['colname']] = {
            'column': col['colname'],
            'ctype': col['ctype'],
            'default': col['default'],
        }
    result = {
        'tablename': tablename,
        'primary_key': primary_key,
        'columns': column_def,
    }
    __import__('pudb').set_trace()
    return result


def main():
    result = parse(sql_statements.SQL_CREATE)
    print(result)


if __name__ == '__main__':
    main()
