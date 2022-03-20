# Project 4 - Queue system

### How many API calls you can handle simultaneously and why?
Looking at the output of `lscpu` that shows 1 physical core and 4 logical ones, I decided to implement a queue system that handles 4 requests at the same time, since there are 4 logical cores. 

### For example, run different API calls at the same time?
The server will handle 4 API calls at the same time

### Split the processing of an API into multiple threads or process?
Each API call is going to be handled inside a separate process (even though I only have one physical CPU) because I prefer each API call to be handled in a process that has its own memory compared to threads.

### Results with 4 requests
When we run the system with 4 API requests:
![8-requests-screenshot](https://github.com/pkiourti/queue-system/blob/main/screenshots/8-requests.png)

When we run the system with 10 API requests but we sent a kill signal to the process that handles the last request:
![8-requests-screenshot](https://github.com/pkiourti/queue-system/blob/main/screenshots/screenshot-kill-a-process.png)
