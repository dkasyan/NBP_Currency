def create_table_in_book():
    conn = sqlite3.connect('example.db')
    readings = {}
    c = conn.cursor()
    counter = 0

    # CREATE TABLE[IF NOT EXISTS][schema_name].table_name(
    # column_1 data_type PRIMARY KEY,
# column_2 data_type NOT NULL,
# column_3 data_type DEFAULT 0,
# table_constraints
    # )
    c.execute("""create table if not exists readings (
        ID INTEGER PRIMARY KEY, 
	    PM25 TEXT NOT NULL,
	    PM10 TEXT NOT NULL,
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
