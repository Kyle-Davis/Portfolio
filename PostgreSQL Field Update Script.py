# Kyle Davis
# Created Aug 15, 2018
import psycopg2

# create row iterator function to display query results
def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

# connect to postgresql db
conn = psycopg2.connect(host="host.address", database="design_tool", user="username", password="password")

cur = conn.cursor()
query = "select fqn_id, workorderid, outputports FROM design_tool.city.equipment WHERE outputports IS NULL and isdeleted = 'f' ORDER BY workorderid ASC"
# execute sql query
cur.execute(query)
print("Number of features with null values in outputports column:", cur.rowcount)
for row in iter_row(cur, 10):
    print(row)

# execute sql update
cur.execute("update design_tool.city.equipment set outputports = 432 WHERE outputports IS NULL and isdeleted = 'f'",(432))
# commit updates to database
conn.commit()
# terminate cursor and close connection to DB
cur.close()
conn.close()

