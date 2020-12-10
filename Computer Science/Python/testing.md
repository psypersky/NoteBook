Quick python mock.patch lesson from Lisa Roach sec Eng @ Facebook

Patch where the code lives, not where the code is defined

if you are trying to patch the function of a library like so

```@mock.patch('app.lib.db.psycopg2')```

do instead

``````