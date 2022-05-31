import sqlalchemy

def create_table_in_book():
    conn = sqlite3.connect('example.db')
    readings = {}
    c = conn.cursor()
    counter = 0
    c.execute("""create table if not exists readings (
        ID INTEGER PRIMARY KEY, 
	    STAT TEXT NOT NULL,
	    CURRE TEXT NOT NULL,
        VALUE TEXT NOT NULL,
        USER TEXT NOT NULL,
        TAG TEXT NOT NULL,
        RICHES TEXT NOT NULL,
        datetime TEXT NOT NULL
    );""")

    while True:
        readings = {}
        readings["PM25"] = round(random.uniform(0, 121), 1)
        readings["PM10"] = round(random.uniform(0, 201), 1)
        readings["datetime"] = time.strftime('%Y-%m-%d')

        c.execute("INSERT INTO readings VALUES (?,?,?,?)",
                  (counter, readings["datetime"], readings["PM25"], readings["PM10"]))

        conn.commit()

        counter += 1
        if counter == 100:
            break
