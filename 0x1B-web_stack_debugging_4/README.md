0x1B. Web stack debugging #4
============================

-   By Sylvain Kalache, co-founder at Holberton School
-   Weight: 1

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/313/frdkCrb.jpg)

Requirements
------------

### General

-   All your files will be interpreted on Ubuntu 14.04 LTS
-   All your files should end with a new line
-   A `README.md` file at the root of the folder of the project is mandatory
-   Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors
-   Your Puppet manifests must run without error
-   Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
-   Your Puppet manifests files must end with the extension `.pp`
-   Files will be checked with Puppet v3.4

### Install `puppet-lint`

```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1

```

Tasks
-----

### 0\. Sky is the limit, let's bring that limit higher

mandatory

In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it's not doing well: we are getting a huge amount of failed requests.

For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 943 requests failed, let's fix our stack so that we get to 0, and remember that when something is going wrong, logs are your best friends!

```
root@0a62aa706eb3:/# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests

Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        201 bytes

Concurrency Level:      100
Time taken for tests:   0.353 seconds
Complete requests:      2000
Failed requests:        943
   (Connect: 0, Receive: 0, Length: 943, Exceptions: 0)
Non-2xx responses:      1057
Total transferred:      1196526 bytes
HTML transferred:       789573 bytes
Requests per second:    5664.01 [#/sec] (mean)
Time per request:       17.655 [ms] (mean)
Time per request:       0.177 [ms] (mean, across all concurrent requests)
Transfer rate:          3309.15 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   1.1      0       8
Processing:     2   17   3.8     17      24
Waiting:        2   17   3.8     17      24
Total:          9   17   3.3     17      24

Percentage of the requests served within a certain time (ms)
  50%     17
  66%     19
  75%     20
  80%     20
  90%     21
  95%     23
  98%     23
  99%     23
 100%     24 (longest request)
root@0a62aa706eb3:/#
root@0a62aa706eb3:/# puppet apply 0-the_sky_is_the_limit_not.pp
Notice: Compiled catalog for 0a62aa706eb3.local in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[fix--for-nginx]/returns: executed successfully
Notice: Finished catalog run in 1.12 seconds
root@0a62aa706eb3:/#
root@0a62aa706eb3:/#
root@0a62aa706eb3:/# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests

Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        612 bytes

Concurrency Level:      100
Time taken for tests:   0.301 seconds
Complete requests:      2000
Failed requests:        0
Total transferred:      1706000 bytes
HTML transferred:       1224000 bytes
Requests per second:    6650.99 [#/sec] (mean)
Time per request:       15.035 [ms] (mean)
Time per request:       0.150 [ms] (mean, across all concurrent requests)
Transfer rate:          5540.33 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    4   2.5      3      12
Processing:     2   11   5.2     10      31
Waiting:        1   10   5.2      8      29
Total:          5   15   5.2     14      31

Percentage of the requests served within a certain time (ms)
  50%     14
  66%     17
  75%     18
  80%     19
  90%     22
  95%     26
  98%     27
  99%     28
 100%     31 (longest request)
root@0a62aa706eb3:/#

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x1B-web_stack_debugging_4`
-   File: `0-the_sky_is_the_limit_not.pp`
