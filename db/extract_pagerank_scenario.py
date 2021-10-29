import sqlite3
'''
Script that extracts a pagerank-scenario from a mediawiki-sqlite db and writes it to a file
scenario format (list of lists) is compatible with the iterative page rank script pagerank.py 

by: Philip Machácek, Felix Siegmann @ TBS1
'''
#1) Initialize connection to DB file
con = sqlite3.connect('my_wiki.sqlite')

#2) create cursor
cur = con.cursor()

#3) Initialize dictionary that will hold page ids and the lists of links to them (by id)
scenario = {}

#4) Get all page ids from page table
cur.execute('''
SELECT page_id from page ORDER BY page_id
''')

row = cur.fetchall()

#5) iterate over all returned rows
for r in row:
    #5.1) make entry in dictionary by page id key (empty list)
    scenario[r[0]] = []

    #5.2) get entries from pagelinks table that specifies pages that link to the current page id
    cur.execute('''
    SELECT pl.pl_from FROM pagelinks pl INNER JOIN page p ON pl.pl_title = p.page_title AND p.page_id = ?
    ''', (r[0],))

    #5.3) get returned data
    matches = cur.fetchall()
    
    #5.4) iterate over all returned rows
    for n in matches:
        #5.5) write ids that link to our page to the list for this page
        scenario[r[0]].append(n[0])

#6) create outfile
with open('mediawiki_scenario.txt', 'w+') as f:
    f.write("[")
    #6.1) go through dictionary and write entries to file as list
    for k in scenario.keys():
        f.write(str(scenario[k]) + ",")
    f.write("]")

