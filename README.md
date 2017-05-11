# lineserver
---
## How does your system work? (if not addressed in comments in source)
The system reads the file and inserts each line into a database prior to launch. This allows us to use the database indexing to access a line instead of iterating over the file each time.
If the row can fit in memory then it can also fit in a sqlite TEXT columns:
http://www.sqlite.org/limits.html
I use the standard sqlite rowid indexing (look up uses a b-tree):
http://www.sqlite.org/rowidtable.html

Some caching is done at the flask app level to optimize repeated requests.
This cache size can be set in config.py - currently defaults to 1GB.

## What do we need to build your system?
The app should build and run on any UNIX system with Python and pip installed.

Python v3.5.0 was used to develop and test.

## How will your system perform with a 1 GB file? a 10 GB file? a 100 GB file?
 A 1 GB file should easily fit in memory, which would make the system quite fast as it does not need to make calls to the database. The larger the file, the smaller the cache will have an effect (Unless we use a server with 128GB mem or distributed cache).
 The biggest bottleneck will be the file processing time. Inserting row by row would take quite a while for a 100GB file. This could be optimized fairly easily if we can make assumptions about the maximum size of each line and system memory available.

## How will your system perform with 100 users? 10000 users? 1000000 users?
 Flask is not great at handling a lot of simultaneous connections. Prior to mass usage the system should be adapted to use gunicorn and nginx (or any other WSGI - load balancer stack)

## What documentation, websites, papers, etc did you consult in doing this assignment?
 I had to refresh my memory on sqlite to make sure it would fit the requirements of the system (Links above).
 Test data file came from https://www.bitmex.com/app/index/.ZECXBT
 Otherwise I mainly consulted prior work

## What third-party libraries or other tools does the system use? How did you choose each library or framework you used?
 The system uses Flask, sqlite, and other standard python libraries. These libraries were chosen mostly for their simplicity.

## How long did you spend on this exercise? If you had unlimited more time to spend on this, how would you spend it and how would you prioritize each item?
 I spent around 5 hours on this project. If given unlimited time, I would prioritize the implementation of gunicorn and redis, which would get the system closer to supporting mass scale. In a "real-life" scenario, it would be extremely useful to launch as a prototype and analyse patterns of usage (e.g. Are users making a large amount of requests sporadically? potential batch endpoint) and then optimizing accordingly. Thinking about the business goals and problems that the lineserver is trying to address would be key.

## If you were to critique your code, what would you have to say about it?
 The general architecture covers the basic needs of the server and attempts to make high level optimizations (e.g. pre-processing the file and using a database for indexing/IO, caching to speed up repeated requests). However, the choice of tools is largely based on a 1-server deployment. To run at scale, a lot of these tools would have to be replaced. Some suggestions would be a distributed DB (postgres, cassandra) instead of sqlite, distributed REDIS for caching, and an elastic load balancer on top of nginx/gunicorn/flask.


