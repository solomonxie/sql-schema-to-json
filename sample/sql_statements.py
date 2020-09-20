SQL_CREATE = '''
    CREATE TABLE "some_table" (
        "tbid" FLOAT NOT NULL,
        "alist" ARRAY NOT NULL,
        "updated_time" timestamp,
        PRIMARY KEY ("tbid")
    );
'''
