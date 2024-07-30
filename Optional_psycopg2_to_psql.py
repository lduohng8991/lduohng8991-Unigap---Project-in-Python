import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'suppliers'
username = 'hong'
passw = '01222036125'
port_id = 5432
conn = None
cur = None

conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = passw,
            port = port_id, 
            cursor_factory=psycopg2.extensions.cursor
                                )

try:
    with conn:         
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cur.execute('DROP TABLE IF EXISTS game_demo')

            create_script = '''
                            CREATE TABLE IF NOT EXISTS game_demo(
                                                    ID INT NOT NULL PRIMARY KEY, 
                                                    date_time TIMESTAMP NULL, 
                                                    event_name VARCHAR(40) NULL, 
                                                    level INT NULL, 
                                                    "user" VARCHAR(255) NULL, 
                                                    day_diff INT NULL, 
                                                    day0 TIMESTAMP NULL, 
                                                    mode_game VARCHAR(30) NULL, 
                                                    win VARCHAR(30) NULL, 
                                                    reason_to_die VARCHAR(30) NULL, 
                                                    quantity INT NULL, 
                                                    version VARCHAR(10) NULL                            
                                                                        )
                            '''
            cur.execute(create_script)

            insert_script = '''
                            INSERT INTO game_demo (ID, date_time, event_name, level, "user", day_diff, day0, mode_game, win, reason_to_die, quantity, version)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            '''
            insert_values =  [ 
                                (40, '10/28/2023', 'game_start', 1, '1cffd052-4616-4d29-bfd5-950e23b763d4', 0, '10/28/2023', 'normal', '', '', 0, '1.6.0'), 
                                (41, '10/28/2023', 'game_start', 1, '1cffd052-4616-4d29-bfd5-950e23b763d4', 0, '10/28/2023', 'normal', '', '', 0, '1.6.0'), 
                                (42, '10/28/2023', 'game_start', 2, '1cffd052-4616-4d29-bfd5-950e23b763d4', 0, '10/28/2023', 'normal', '', '', 0, '1.6.0')
                                    ]
            for record in insert_values:
                cur.execute(insert_script, record)

            delete_smthng = 'DELETE FROM game_demo WHERE ID = %s'
            delete_record = ('40', )
            cur.execute(delete_smthng, delete_record)    

            cur.execute('SELECT * FROM game_demo')
            for col in cur.fetchall():
                print(col['ID'], 
                    col['date_time'],
                    col["user"],
                    col['mode_game'],
                    col['win'], 
                    col['version'])

            conn.commit()

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
