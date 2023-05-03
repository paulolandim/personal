import sqlparse

def has_where_clause(stmt):
    if not isinstance(stmt, sqlparse.sql.Statement):
        return False
    if not stmt.get_type() == 'UPDATE':
        return False
    return any(isinstance(t, sqlparse.sql.Where) for t in stmt.tokens)
    
# Split a string containing two SQL statements:
raw = """
    UPDATE customers SET age = 20 WHERE id = 1; UPDATE customers SET age = 25 WHERE id = 2;
    UPDATE customers SET age = 18 id = 3;
""" 
statements = sqlparse.split(raw)
i = 0
n = 0
while i <= 2:  
    first = statements[i]
    r = sqlparse.format(first, keyword_case='upper')
    if has_where_clause(sqlparse.parse(r)[0]):
       n += 1 #print("Statement has a WHERE clause")#
    else:
        print("Statement does not have a WHERE clause in line : " + str(i+1))
    i = i+1
print("Número de Statements com where: " + str(n))    
     
