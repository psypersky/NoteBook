# The with statement
# https://docs.python.org/3/whatsnew/2.6.html#pep-343-the-with-statement

# Instead of try/finally to cleanup resources you can use a with statement
# open returns a context manager
# __enter()__ assigns a file object to f
# with-block is executed
# __exit()__ closes file object even if error happened
with open("myfile.txt") as f:
    for line in f:
        print(line)

# Writting Context Managers

# he contextlib module also has a nested(mgr1, mgr2, ...) function
# that combines a number of context managers so you don’t need to write
# nested ‘with’ statements.

# https://docs.python.org/3/whatsnew/2.6.html#writing-context-managers
# TODO

# lock = threading.Lock()
# with nested (db_transaction(db), lock) as (cursor, locked):
#     ...