0x01. Shell, permissions
========================

-   By Julien Barbier
-   Weight: 1
-   Project over - took place from 08-19-2021 to 08-20-2021.


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


