0x18. Webstack monitoring
=========================

-   By Sylvain Kalache, co-founder at Holberton School
-   Weight: 1

Concepts
--------

*For this project, students are expected to look at these concepts:*

-   [Monitoring](https://alx-intranet.hbtn.io/concepts/13)
-   [Server](https://alx-intranet.hbtn.io/concepts/67)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/hb3pAsO.png)

Background Context
------------------

"You cannot fix or improve what you cannot measure" is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

Web stack monitoring can be broken down into 2 categories:

-   Application monitoring: getting data about your running software and making sure it is behaving as expected
-   Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/ktCXnhE.jpg)

Resources
---------

**Read or watch**:

-   [What is server monitoring](https://alx-intranet.hbtn.io/rltoken/km_XUDAfXEBoXZQsIWEo5Q "What is server monitoring")
-   [What is application monitoring](https://alx-intranet.hbtn.io/rltoken/z9jsikINjrsUo2QY5_Xz8g "What is application monitoring")
-   [System monitoring by Google](https://alx-intranet.hbtn.io/rltoken/_8KIbIUNzMgKi_LiGMBWAw "System monitoring by Google")
-   [Nginx logging and monitoring](https://alx-intranet.hbtn.io/rltoken/V3GsrDcMHPdgrizShj4RCg "Nginx logging and monitoring")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/Bd9r8twsVT3S_8j7-kOLrg "explain to anyone"), **without the help of Google**:

### General

-   Why is monitoring needed
-   What are the 2 main area of monitoring
-   What are access logs for a web server (such as Nginx)
-   What are error logs for a web server (such as Nginx)

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted on Ubuntu 16.04 LTS
-   All your files should end with a new line
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   All your Bash script files must be executable
-   Your Bash script must pass `Shellcheck` (version `0.3.7`) without any error
-   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
-   The second line of all your Bash scripts should be a comment explaining what is the script doing

Your servers
------------

| Name | Username | IP | State |  |
| --- | --- | --- | --- | --- |
| 1733-web-01 | `ubuntu` | `3.235.21.36` | running |

Actions Toggle Dropdown

 |
| 1733-web-02 | `ubuntu` | `34.139.50.126` | running |

Actions Toggle Dropdown

 |
| 1733-lb-01 | `ubuntu` | `34.231.109.143` | running |

Actions Toggle Dropdown

 |

Tasks
-----

### 0\. Sign up for Datadog and install datadog-agent

mandatory

For this task head to [https://www.datadoghq.com/](https://alx-intranet.hbtn.io/rltoken/Ufs6rTHMET5LB1Uoylx0nw "https://www.datadoghq.com/") and sign up for a free `Datadog` account. When signing up, you'll have the option of selecting statistics from your current stack that `Datadog` can monitor for you. Once you have an account set up, follow the instructions given on the website to install the `Datadog` agent.

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6b0ea6345a6375437845.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220427%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220427T130149Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=86c64b984731615d21270480982a860bec76296c42fd68d42ae39d79c5be887b)

-   Sign up for Datadog - **Please make sure you are using the US website of Datagog (.com)**
-   Install `datadog-agent` on `web-01`
-   Create an `application key`
-   Copy-paste in your Intranet user profile ([here](https://alx-intranet.hbtn.io/rltoken/elXu5CcaGpeK7GxerBb7wQ "here")) your DataDog `API key` and your DataDog `application key`.
-   Your server `web-01` should be visible in Datadog under the host name `XX-web-01`
    -   You can validate it by using this [API](https://alx-intranet.hbtn.io/rltoken/5BtVPmgzhb96y7jZDGGHOQ "API")
    -   If needed, you will need to update the hostname of your server

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x18-webstack_monitoring`

 Done? Help Check your code Get a sandbox

### 1\. Monitor some metrics

mandatory

Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some `monitors` within the `Datadog` dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: [System Check](https://alx-intranet.hbtn.io/rltoken/4RPOEVDTqKXuvyU4Gkj2Bw "System Check").

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6a4551974aadc181e97a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220427%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220427T130149Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9b45110b10a0c978f71c1c446f26aa6f4feda9f27225cdac4da0bade05a4107e)

-   Set up a monitor that checks the number of read requests issued to the device per second.
-   Set up a monitor that checks the number of write requests issued to the device per second.

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x18-webstack_monitoring`

 Done? Help Check your code Get a sandbox

### 2\. Create a dashboard

mandatory

Now create a dashboard with different metrics displayed in order to get a few different visualizations.

-   Create a new `dashboard`
-   Add at least 4 `widgets` to your dashboard. They can be of any type and monitor whatever you'd like
-   Create the answer file `2-setup_datadog` which has the `dashboard_id` on the first line. **Note**: in order to get the id of your dashboard, you may need to use [Datadog's API](https://alx-intranet.hbtn.io/rltoken/QhlPcQqUocwWcOkZ9s4mWQ "Datadog's API")

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x18-webstack_monitoring`
-   File: `2-setup_datadog`
