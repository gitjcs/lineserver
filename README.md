# lineserver

How does your system work? (if not addressed in comments in source)
• What do we need to build your system?
• How will your system perform with a 1 GB file? a 10 GB file? a 100 GB file?
 A 1 GB file should easily fit in memory, which would make the system quite fast as it does not need to make calls to the database.
• How will your system perform with 100 users? 10000 users? 1000000 users?
• What documentation, websites, papers, etc did you consult in doing this
assignment?
• What third-party libraries or other tools does the system use? How did you
choose each library or framework you used?
• How long did you spend on this exercise? If you had unlimited more time to
spend on this, how would you spend it and how would you prioritize each item?
 I apent around 4 hours on this project. If given unlimited time, it would be extremely useful to analyse patterns of usage (e.g. Are users making a large amount of requests sporadically? potential batch endpoint)
• If you were to critique your code, what would you have to say about it?
 The general system architecture covers the basic needs of the server and attempts to make high level optimizations (e.g. pre-processing the file and using a database for indexing/IO, caching to speed up repeated requests). However, the choice of tools is largely based on a 1-server deployment. To run at scale, a lot of these tools would have to be replaced. Some suggestions would be a distributed DB (postgres, cassandra) instead of sqlite, distributed REDIS for caching, and an elastic load balancer on top of nginx/gunicorn/flask.
