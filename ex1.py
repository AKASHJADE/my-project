import MySQLdb as mdb


try:
    con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
        
    con.query("SELECT VERSION()")
    result = con.use_result()
    
    print ("MySQL version: %s" )
    result.fetch_row()[0]
    


finally:
    
    if con:
        con.close()
