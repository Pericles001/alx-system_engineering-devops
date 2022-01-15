0x04. Loops, conditions and parsing
===================================

-   By Sylvain Kalache
-   Weight: 1
-   Ongoing second chance project - started 01-13-2022, must end by 01-18-2022 (in 2 days) - you're done with 0% of tasks.
-   QA review fully automated.

#### In a nutshell...

-   **Auto QA review:** 0.0/83 mandatory & 0.0/30 optional
-   **Altogether:**  **0.0%**
    -   Mandatory: 0.0%
    -   Optional: 0.0%
    -   Calculation:  0.0% + (0.0% * 0.0%)  == **0.0%**

About Bash projects
-------------------

Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.

Background Context
------------------

[![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/b07e3333b1edfb9beed5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220115%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220115T182752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9d73d141cd49b81a0d81762b039e1c7d35276c1485e253db49676853cd7426f2)](https://youtu.be/BC2neyc5GcI)

Resources
---------

**Read or watch**:

-   [Loops sample](https://alx-intranet.hbtn.io/rltoken/wT98UJfv_E2tk4yP9PcLLw "The <code>for</code> loop" target="_blank">The <code>for</code> loop</a> </li>
    <li><a href=")
-   [Variable assignment and arithmetic](https://alx-intranet.hbtn.io/rltoken/olvOKX699pq50rkHRE5cSA "Variable assignment and arithmetic")
-   [Comparison operators](https://alx-intranet.hbtn.io/rltoken/HxohzllkOWh0t4dy_HptIQ "Comparison operators")
-   [File test operators](https://alx-intranet.hbtn.io/rltoken/g8of2ABPEJfCNtPrDQaqVw "File test operators")
-   [Make your scripts portable](https://alx-intranet.hbtn.io/rltoken/O0Ay21p7tDhfLMsYbtAKug "Make your scripts portable")

**man or help**:

-   `env`
-   `cut`
-   `for`
-   `while`
-   `until`
-   `if`

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/UnkzDNdH09TFJ0-Y56azyg "explain to anyone"), **without the help of Google**:

### General

-   How to create SSH keys
-   What is the advantage of using `#!/usr/bin/env bash` over `#!/bin/bash`
-   How to use `while`, `until` and `for` loops
-   How to use `if`, `else`, `elif` and `case` condition statements
-   How to use the `cut` command
-   What are files and other comparison operators, and how to use them

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted on Ubuntu 20.04 LTS
-   All your files should end with a new line
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   All your Bash script files must be executable
-   You are not allowed to use `awk`
-   Your Bash script must pass `Shellcheck` (version `0.7.0`) without any error
-   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
-   The second line of all your Bash scripts should be a comment explaining what is the script doing

More Info
---------

### Shellcheck

[Shellcheck](https://alx-intranet.hbtn.io/rltoken/joK6l_yEZ9N7T0GQ1RDjLA "Shellcheck") is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. `Shellcheck` is your friend! **All your Bash scripts must pass `Shellcheck` without any error or you will not get any points on the task**.

`Shellcheck` is available on the school's computers. If you want to use it on your own computer, here is how to [install it](https://alx-intranet.hbtn.io/rltoken/jbz0_-i3TV3WpKgxhyrtpA "install it").

Examples:

Not passing `Shellcheck`:

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/Vxotqyj.png)

Passing `Shellcheck`:

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/ubHWxDU.png)

For every feedback, Shellcheck will provide a code that you can use to get more information about the issue, for example for code `SC2034`, you can browse [https://github.com/koalaman/shellcheck/wiki/SC2034](https://alx-intranet.hbtn.io/rltoken/dxp49_rfO4_9Yjtcg59exg "https://github.com/koalaman/shellcheck/wiki/SC2034").

Tasks
-----

### 0\. Create a SSH RSA key pair

mandatory

Score: 0.00% (Checks completed: 0.00%)

Read for this task:

-   [Linux and Mac OS users](https://alx-intranet.hbtn.io/rltoken/Cy1plV2eR3VphjPqliXB8A "Linux and Mac OS users")
-   [Windows users](https://alx-intranet.hbtn.io/rltoken/PXriGT0IKaSXC7L5l0CVag "Windows users")

man: `ssh-keygen`

You will soon have to manage your own **servers** concept page hosted on remote [data centers](https://alx-intranet.hbtn.io/rltoken/nDPzEm5SYxcdGxP_OpVYXQ "data centers"). We need to set them up with your RSA public key so that you can access them via SSH.

Create a RSA key pair.

Requirements:

-   Share your **public key** in your answer file `0-RSA_public_key.pub`
-   Fill the `SSH public key` field of your [intranet profile](https://alx-intranet.hbtn.io/rltoken/qsaEQ3ZWrgs-zoueDpXpPA "intranet profile") with the public key you just generated
-   **Keep the private key to yourself in a secure location**, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
-   If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase

SSH and RSA keys will be covered in depth in a later project.

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x04-loops_conditions_and_parsing`
-   File: `0-RSA_public_key.pub`

 Done? Help Check your code Get a sandbox QA Review

### 1\. For Best School loop

mandatory

Score: 0.00% (Checks completed: 0.00%)

Write a Bash script that displays `Best School` 10 times.

Requirement:

-   You must use the `for` loop (`while` and `until` are forbidden)

```
sylvain@ubuntu$ head -n 2 1-for_best_school
#!/usr/bin/env bash
# This script is displaying "Best School" 10 times
sylvain@ubuntu$ ./1-for_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$

```

Note that:

-   The first line of my Bash script starts with `#!/usr/bin/env bash`
-   The second line of my Bash scripts is a comment explaining what it is doing

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x04-loops_conditions_and_parsing`
-   File: `1-for_best_school`

 Done? Help Check your code Get a sandbox QA Review

### 2\. While Best School loop

mandatory

Score: 0.00% (Checks completed: 0.00%)

Write a Bash script that displays `Best School` 10 times.

Requirements:

-   You must use the `while` loop (`for` and `until` are forbidden)

```
sylvain@ubuntu$ ./2-while_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x04-loops_conditions_and_parsing`
-   File: `2-while_best_school`

 Done? Help Check your code Get a sandbox QA Review

### 3\. Until Best School loop

mandatory

Score: 0.00% (Checks completed: 0.00%)

Write a Bash script that displays `Best School` 10 times.

Requirements:

-   You must use the `until` loop (`for` and `while` are forbidden)

```
sylvain@ubuntu$ ./3-until_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x04-loops_conditions_and_parsing`
-   File: `3-until_best_school`

 Done? Help Check your code Get a sandbox QA Review

### 4\. If 9, say Hi!

mandatory

Score: 0.00% (Checks completed: 0.00%)

Write a Bash script that displays `Best School` 10 times, but for the 9th iteration, displays `Best School` *and then* `Hi` on a new line.

Requirements:

-   You must use the `while` loop (`for` and `until` are forbidden)
-   You must use the `if` statement

```
sylvain@ubuntu$ ./4-if_9_say_hi
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Hi
Best School
sylvain@ubuntu$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x04-loops_conditions_and_parsing`
-   File: `4-if_9_say_hi`

 Done? Help Check your code Get a sandbox QA Review

### 5\. 4 bad luck, 8 is your chance

mandatory

Score: 0.00% (Checks completed: 0.00%)

Write a Bash script that loops from 1 to 10 and:

-   displays `bad luck` for the 4th loop iteration
-   displays `good luck` for the 8th loop iteration
-   displays `Best School` for the other iterations

Requirements:

-   You must use the `while` loop (`for` and `until` are forbidden)
-   You must use the `if`, `elif` and `else` statements

```
sylvain@ubuntu$ ./5-4_bad_luck_8_is_your_chance
Best School
Best School
Best School
bad luck
Best School
Best School
Best School
good luck
Best School
Best School
sylvain@ubuntu$

```

For the most curious:

-   [8 in the Chinese culture](https://alx-intranet.hbtn.io/rltoken/uhCfz6ariijQvbvmCyYRMg "8 in the Chinese culture")
-   [4 in the Chinese culture](https://alx-intranet.hbtn.io/rltoken/WwpjD57ABmwWSfdUVcBhNg "4 in the Chinese culture")

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x04-loops_conditions_and_parsing`
-   File: `5-4_bad_luck_8_is_your_chance`

 Done? Help Check your code Get a sandbox QA Review

### 6\. Superstitious numbers

mandatory

Score: 0.00% (Checks completed: 0.00%)

Write a Bash script that displays numbers from 1 to 20 and:

-   displays `4` *and then* `bad luck from China` for the 4th loop iteration
-   displays `9` *and then* `bad luck from Japan` for the 9th loop iteration
-   displays `17` *and then* `bad luck from Italy` for the 17th loop iteration

Requirements:

-   You must use the `while` loop (`for` and `until` are forbidden)
-   You must use the `case` statement

```
sylvain@ubuntu$ ./6-superstitious_numbers
1
2
3
4
bad luck from China
5
6
7
8
9
bad luck from Japan
10
11
12
13
14
15
16
17
bad luck from Italy
18
19
20
sylvain@ubuntu$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x04-loops_conditions_and_parsing`
-   File: `6-superstitious_numbers`

 Done? Help Check your code Get a sandbox QA Review

### 7\. Clock

mandatory

Score: 0.00% (Checks completed: 0.00%)

Write a Bash script that displays the time for 12 hours and 59 minutes:

-   display hours from 0 to 12
-   display minutes from 1 to 59

Requirements:

-   You must use the `while` loop (`for` and `until` are forbidden)

Note that in this example, we only display the first 70 lines using the `head` command.

```
sylvain@ubuntu$ ./7-clock | head -n 70
Hour: 0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
Hour: 1
1
2
3
4
5
6
7
8
9
sylvain@ubuntu$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x04-loops_conditions_and_parsing`
-   File: `7-clock`

 Done? Help Check your code Get a sandbox QA Review

### 8\. For ls

mandatory

Score: 0.00% (Checks completed: 0.00%)

Write a Bash script that displays:

-   The content of the current directory
-   In a list format
-   Where only the part of the name after the first dash is displayed (refer to the example)

Requirements:

-   You must use the `for` loop (`while` and `until` are forbidden)
-   Do not display hidden files

```
sylvain@ubuntu$ ls
100-read_and_cut              1-for_best_school         6-superstitious_numbers
101-tell_the_story_of_passwd  2-while_best_school       7-clock
102-lets_parse_apache_logs    3-until_best_school       8-for_ls
103-dig_the-data              4-if_9_say_hi                  9-to_file_or_not_to_file
10-fizzbuzz                   5-4_bad_luck_8_is_your_chance
sylvain@ubuntu$  ./8-for_ls
read_and_cut
tell_the_story_of_passwd
lets_parse_apache_logs
dig_the-data
fizzbuzz
for_best_school
while_best_school
until_best_school
if_9_say_hi
4_bad_luck_8_is_your_chance
superstitious_numbers
clock
for_ls
to_file_or_not_to_file
sylvain@ubuntu$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x04-loops_conditions_and_parsing`
-   File: `8-for_ls`

 Done? Help Check your code Get a sandbox QA Review

### 9\. To file, or not to file

mandatory

Score: 0.00% (Checks completed: 0.00%)

Write a Bash script that gives you information about the `school` file.

Requirements:

-   You must use `if` and, `else` (`case` is forbidden)
-   Your Bash script should check if the file exists and print:
    -   if the file exists: `school file exists`
    -   if the file does not exist: `school file does not exist`
-   If the file exists, print:
    -   if the file is empty: `school file is empty`
    -   if the file is not empty: `school file is not empty`
    -   if the file is a regular file: `school is a regular file`
    -   if the file is not a regular file: (nothing)

```
sylvain@ubuntu$ file school
school: cannot open `school' (No such file or directory)
sylvain@ubuntu$ ./9-to_file_or_not_to_file
school file does not exist
sylvain@ubuntu$ touch school
sylvain@ubuntu$ ./9-to_file_or_not_to_file
school file exists
school file is empty
school is a regular file
sylvain@ubuntu$ echo 'betty' > school
sylvain@ubuntu$ ./9-to_file_or_not_to_file
school file exists
school file is not empty
school is a regular file
sylvain@ubuntu$ rm school
sylvain@ubuntu$ mkdir school
sylvain@ubuntu$ ./9-to_file_or_not_to_file
school file exists
school file is not empty
sylvain@ubuntu$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x04-loops_conditions_and_parsing`
-   File: `9-to_file_or_not_to_file`

 Done? Help Check your code Get a sandbox QA Review

### 10\. FizzBuzz

mandatory

Score: 0.00% (Checks completed: 0.00%)

Write a Bash script that displays numbers from 1 to 100.

Requirements:

-   Displays `FizzBuzz` when the number is a multiple of 3 and 5
-   Displays `Fizz` when the number is multiple of 3
-   Displays `Buzz` when the number is a multiple of 5
-   Otherwise, displays the number
-   In a list format

```
sylvain@ubuntu$ ./10-fizzbuzz | head -20
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
sylvain@ubuntu$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x04-loops_conditions_and_parsing`
-   File: `10-fizzbuzz`