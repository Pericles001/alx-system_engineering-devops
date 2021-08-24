0x01. Shell, permissions
========================

-   By Julien Barbier
-   Weight: 1



About Bash projects
-------------------

Unless stated, all your projects will be auto-corrected with Ubuntu 14.04 LTS.

Resources
---------

**Read or watch**:

-   [Permissions](https://alx-intranet.hbtn.io/rltoken/aQmRB6ms-SDHUhqY0Rsa3g "Permissions")

**man or help**:

-   `chmod`
-   `sudo`
-   `su`
-   `chown`
-   `chgrp`
-   `id`
-   `groups`
-   `whoami`
-   `adduser`
-   `useradd`
-   `addgroup`

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/JYGwUPrMzpHfX4U8kUTIxw "explain to anyone"), **without the help of Google**:

### Permissions

-   What do the commands `chmod`, `sudo`, `su`, `chown`, `chgrp` do
-   Linux file permissions
-   How to represent each of the three sets of permissions (owner, group, and other) as a single digit
-   How to change permissions, owner and group of a file
-   Why can't a normal user `chown` a file
-   How to run a command with root privileges
-   How to change user ID or become superuser

### Other Man Pages

-   How to create a user
-   How to create a group
-   How to print real and effective user and group IDs
-   How to print the groups a user is in
-   How to print the effective userid

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your scripts will be tested on Ubuntu 20.04 LTS
-   All your scripts should be exactly two lines long (`$ wc -l file` should print 2)
-   All your files should end with a new line ([why?](http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
-   The first line of all your files should be exactly `#!/bin/bash`
-   A `README.md` file, at the root of the folder of the project, describing what each script is doing
-   You are not allowed to use backticks, `&&`, `||` or `;`
-   All your files must be executable

### Description
  This project covers basic esercises about shell permission commands 

### Structure
   * 0-iam_betty : change user ID to betty
   * 1-who_am_i : prints the effective user id of current user
   * 2-groups : prints all groups of current user
   * 3-new_owner : changes owner of file hello to user betty
   * 4-empty : creates an empty file called hello
   * 5-execute : add execute permission to owner of the file hello
   * 6-multiple_permisssions : add execute permission to the owner and group owner, and read permission to other users for the file hello
   * 7-everybody : add execute permission to the owner, group owner, and other users for the file hello
   * 8-James_Bond : gives all the permission to other users but no permission for the owner and group owner for the file hello
   * 9-John_Doe : gives all permission to the owner, reading and execution to the group owner, and writing and execution to other users for the file hello
   * 10-mirror_permissions : sets the mode of file hello the same as olleh's mode
   * 11-directories_permissions : adds execute permission to all subdirectories of current directory for the owner, group owner and other users
   * 12-directory_permissions : create a directory dir_holberton with 751 permission
   * 13-change_group : changes group owner to holberton for the file hello
   * 14-change_owner_and_group : change owner to betty and group owner to holberton for all files and directories in the working directory
   * 15-symbolic_link_permissions : change file _hello's owner to betty and group owner to holberton
   * 16-if_only : changes owner of file hello to betty only if it is owned by user guillaume
   * 100-Star_Wars :  play the StarWars IV episode in the terminal

Tasks
-----

### 0\. My name is Betty

mandatory

Score: 100.00% (Checks completed: 100.00%)

Create a script that switches the current user to the user `betty`.

-   You should use exactly 8 characters for your command (+1 character for the new line)
-   You can assume that the user `betty` will exist when we will run your script

```
julien@ubuntu:/tmp/h$ tail -1 0-iam_betty | wc -c
9
julien@ubuntu:/tmp/h$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: `0-iam_betty`

 Done! Help Re-check your code Get a sandbox QA Review

### 1\. Who am I

mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a script that prints the effective username of the current user.

```
julien@ubuntu:/tmp/h$ ./1-who_am_i
julien
julien@ubuntu:/tmp/h$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: `1-who_am_i`

 Done! Help Re-check your code Get a sandbox QA Review

### 2\. Groups

mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a script that prints all the groups the current user is part of.

```
julien@ubuntu:/tmp/h$ ./2-groups
julien adm cdrom sudo dip plugdev lpadmin sambashare
julien@ubuntu:/tmp/h$

```

Note: depending on the user, you will get a different output.

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: `2-groups`

 Done! Help Re-check your code Get a sandbox QA Review

### 3\. New owner

mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a script that changes the owner of the file `hello` to the user `betty`.

```
julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 30 Sep 20 14:23 3-new_owner
-rw-rw-r-- 1 julien julien  0 Sep 20 14:18 hello
julien@ubuntu:/tmp/h$ sudo ./3-new_owner
julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 30 Sep 20 14:23 3-new_owner
-rw-rw-r-- 1 betty  julien  0 Sep 20 14:18 hello
julien@ubuntu:/tmp/h$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: `3-new_owner`

 Done! Help Re-check your code Get a sandbox QA Review

### 4\. Empty!

mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a script that creates an empty file called `hello`.

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: `4-empty`

 Done! Help Re-check your code Get a sandbox QA Review

### 5\. Execute

mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a script that adds execute permission to the owner of the file `hello`.

-   The file `hello` will be in the working directory

```
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:26 5-execute
-rw-rw-r-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./hello
bash: ./hello: Permission denied
julien@ubuntu:/tmp/h$ ./5-execute
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:26 5-execute
-rwxrw-r-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: `5-execute`

 Done! Help Re-check your code Get a sandbox QA Review

### 6\. Multiple permissions

mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.

-   The file `hello` will be in the working directory

```
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 36 Sep 20 14:31 6-multiple_permissions
-r--r----- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./6-multiple_permissions
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 36 Sep 20 14:31 6-multiple_permissions
-r-xr-xr-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: `6-multiple_permissions`

 Done! Help Re-check your code Get a sandbox QA Review

### 7\. Everybody!

mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a script that adds execution permission to the owner, the group owner and the other users, to the file `hello`

-   The file `hello` will be in the working directory
-   You are not allowed to use commas for this script

```
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:35 7-everybody
-rw-r----- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./7-everybody
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:35 7-everybody
-rwxr-x--x 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: `7-everybody`

 Done! Help Re-check your code Get a sandbox QA Review

### 8\. James Bond

mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a script that sets the permission to the file `hello` as follows:

-   Owner: no permission at all
-   Group: no permission at all
-   Other users: all the permissions

The file `hello` will be in the working directory You are not allowed to use commas for this script

```
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:40 8-James_Bond
-rwxr-x--x 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./8-James_Bond
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:40 8-James_Bond
-------rwx 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: `8-James_Bond`

 Done! Help Re-check your code Get a sandbox QA Review

### 9\. John Doe

mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a script that sets the mode of the file `hello` to this:

```
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello

```

-   The file `hello` will be in the working directory
-   You are not allowed to use commas for this script

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: `9-John_Doe`

 Done! Help Re-check your code Get a sandbox QA Review

### 10\. Look in the mirror

mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a script that sets the mode of the file `hello` the same as `olleh`'s mode.

-   The file `hello` will be in the working directory
-   The file `olleh` will be in the working directory

```
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 42 Sep 20 14:45 10-mirror_permissions
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
-rw-rw-r-- 1 julien julien  0 Sep 20 14:43 olleh
julien@ubuntu:/tmp/h$ ./10-mirror_permissions
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 42 Sep 20 14:45 10-mirror_permissions
-rw-rw-r-- 1 julien julien 23 Sep 20 14:25 hello
-rw-rw-r-- 1 julien julien  0 Sep 20 14:43 olleh
julien@ubuntu:/tmp/h$

```

Note: the mode of `olleh` will not always be 664. Make sure your script works for any mode.

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: `10-mirror_permissions`

 Done! Help Re-check your code Get a sandbox QA Review

### 11\. Directories

mandatory

Score: 100.00% (Checks completed: 100.00%)

Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.

```
julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   24 Sep 20 14:53 11-directories_permissions
drwx------ 2 julien julien 4096 Sep 20 14:49 dir0
drwx------ 2 julien julien 4096 Sep 20 14:49 dir1
drwx------ 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./11-directories_permissions
julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   24 Sep 20 14:53 11-directories_permissions
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: `11-directories_permissions`

 Done! Help Re-check your code Get a sandbox QA Review

### 12\. More directories

mandatory

Score: 100.00% (Checks completed: 100.00%)

Create a script that creates a directory called `my_dir` with permissions 751 in the working directory.

```
julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   39 Sep 20 14:59 12-directory_permissions
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./12-directory_permission s
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   39 Sep 20 14:59 12-directory_permissions
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien 4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: `12-directory_permissions`

 Done! Help Re-check your code Get a sandbox QA Review

### 13\. Change group

mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a script that changes the group owner to `school` for the file `hello`

-   The file `hello` will be in the working directory

```
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   34 Sep 20 15:03 13-change_group
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien 4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ sudo ./13-change_group
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      34 Sep 20 15:03 13-change_group
drwx--x--x 2 julien julien    4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien    4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien    4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien    4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 julien school   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: `13-change_group`

 Done! Help Re-check your code Get a sandbox QA Review

### 14\. Owner and group

#advanced

Score: 100.00% (Checks completed: 100.00%)

Write a script that changes the owner to `vincent` and the group owner to `staff` for all the files and directories in the working directory.

```
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   36 Sep 20 15:06 100-change_owner_and_group
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien 4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ sudo ./100-change_owner_and_group
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 vincent staff   36 Sep 20 15:06 100-change_owner_and_group
drwx--x--x 2 vincent staff 4096 Sep 20 14:49 dir0
drwx--x--x 2 vincent staff 4096 Sep 20 14:49 dir1
drwx--x--x 2 vincent staff 4096 Sep 20 14:49 dir2
drwxr-x--x 2 vincent staff 4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 vincent staff   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: `100-change_owner_and_group`

 Done! Help Re-check your code Get a sandbox QA Review

### 15\. Symbolic links

#advanced

Score: 100.00% (Checks completed: 100.00%)

Write a script that changes the owner and the group owner of `_hello` to `vincent` and `staff` respectively.

-   The file `_hello` is in the working directory
-   The file `_hello` is a symbolic link

```
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   44 Sep 20 15:12 101-symbolic_link_permissions
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
lrwxrwxrwx 1 julien julien    5 Sep 20 15:10 _hello -> hello
julien@ubuntu:/tmp/h$ sudo ./101-symbolic_link_permissions
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      44 Sep 20 15:12 101-symbolic_link_permissions
-rw-rw-r-- 1 julien julien      23 Sep 20 14:25 hello
lrwxrwxrwx 1 vincent  staff    5 Sep 20 15:10 _hello -> hello
julien@ubuntu:/tmp/h$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: `101-symbolic_link_permissions`

 Done! Help Re-check your code Get a sandbox QA Review

### 16\. If only

#advanced

Score: 100.00% (Checks completed: 100.00%)

Write a script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.

-   The file `hello` will be in the working directory

```
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien    julien      47 Sep 20 15:18 102-if_only
-rw-rw-r-- 1 guillaume julien      23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ sudo ./102-if_only
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      47 Sep 20 15:18 102-if_only
-rw-rw-r-- 1 betty  julien      23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$

```

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: `102-if_only`

 Done! Help Re-check your code Get a sandbox QA Review

### 17\. Star Wars

#advanced

Score: 100.00% (Checks completed: 100.00%)

Write a script that will play the StarWars IV episode in the terminal.

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: `103-Star_Wars`

 Done! Help Re-check your code Get a sandbox

