0x00. Shell, basics
===================

-   By Julien Barbier
-   Weight: 1


About Bash projects
-------------------

Unless stated, all your projects will be auto-corrected with Ubuntu 14.04 LTS.

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/205/image.jpg)

Resources
---------

**Read or watch**:

-   [What Is "The Shell"?](https://alx-intranet.hbtn.io/rltoken/vwO91sqNBgRL03BLu-ueiA "What Is "The Shell"?")
-   [Navigation](https://alx-intranet.hbtn.io/rltoken/iblidp7yp6i-QpT8rDXHaA "Navigation")
-   [Looking Around](https://alx-intranet.hbtn.io/rltoken/xEKUCnQsMH0esQ6fJU5vLA "Looking Around")
-   [A Guided Tour](https://alx-intranet.hbtn.io/rltoken/HUhQ73fFR1GOC5nb4r-mDw "A Guided Tour")
-   [Manipulating Files](https://alx-intranet.hbtn.io/rltoken/olv-1tj4d1LA57Z0PrLNvw "Manipulating Files")
-   [Working With Commands](https://alx-intranet.hbtn.io/rltoken/zUtux3Pm0BkvtwXzbTtkmA "Working With Commands")
-   [Reading Man pages](https://alx-intranet.hbtn.io/rltoken/rddGdsqLf8_kRzp12RaD4A "Reading Man pages")
-   [Keyboard shortcuts for Bash](https://alx-intranet.hbtn.io/rltoken/JcsRq7PW6v7SdpPH_N8udQ "Keyboard shortcuts for Bash")
-   [LTS](https://wiki.ubuntu.com/LTS)
-   [Shebang](https://alx-intranet.hbtn.io/rltoken/cE8ZA3kgEaFhB-IDNv31bQ "Shebang")

**man or help**:

-   `cd`
-   `ls`
-   `pwd`
-   `less`
-   `file`
-   `ln`
-   `cp`
-   `mv`
-   `rm`
-   `mkdir`
-   `type`
-   `which`
-   `help`
-   `man`

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/Cn1p1E1_3FRvKpHfiKJ1GQ "explain to anyone"), **without the help of Google**:

### General

-   What does RTFM mean?
-   What is a Shebang

### What is the Shell

-   What is the shell
-   What is the difference between a terminal and a shell
-   What is the shell prompt
-   How to use the history (the basics)

### Navigation

-   What do the commands or built-ins `cd`, `pwd`, `ls` do
-   How to navigate the filesystem
-   What are the . and .. directories
-   What is the working directory, how to print it and how to change it
-   What is the root directory
-   What is the home directory, and how to go there
-   What is the difference between the root directory and the home directory of the user root
-   What are the characteristics of hidden files and how to list them
-   What does the command `cd -` do

### Looking Around

-   What do the commands `ls`, `less`, `file` do
-   How do you use options and arguments with commands
-   Understand the ls long format and how to display it
-   [A Guided Tour](https://alx-intranet.hbtn.io/rltoken/HUhQ73fFR1GOC5nb4r-mDw "A Guided Tour")
-   What does the `ln` command do
-   What do you find in the most common/important directories
-   What is a symbolic link
-   What is a hard link
-   What is the difference between a hard link and a symbolic link

### Manipulating Files

-   What do the commands `cp`, `mv`, `rm`, `mkdir` do
-   What are wildcards and how do they work
-   How to use wildcards

### Working with Commands

-   What do `type`, `which`, `help`, `man` commands do
-   What are the different kinds of commands
-   What is an alias
-   When do you use the command help instead of man

### Reading Man Pages

-   How to read a man page
-   What are man page sections
-   What are the section numbers for User commands, System calls and Library functions

### Keyboard Shortcuts for Bash

-   Common shortcuts for Bash

### LTS

-   What does `LTS` mean?

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your scripts will be tested on Ubuntu 20.04 LTS
-   All your scripts should be exactly two lines long (`$ wc -l file` should print 2)
-   All your files should end with a new line ([why?](http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
-   The first line of all your files should be exactly `#!/bin/bash`
-   A `README.md` file at the root of the repo, containing a description of the repository
-   A `README.md` file, at the root of the folder of *this* project, describing what each script is doing
-   You are not allowed to use backticks, `&&`, `||` or `;`
-   All your scripts must be executable. To make your file executable, use the `chmod` command: `chmod u+x file`. Later, we'll learn more about how to utilize this command.

More Info
---------

*Example of line count and first line*

```
julien@ubuntu:/tmp$ wc -l 12-file_type
2 12-file_type
julien@ubuntu:/tmp$ head -n 1 12-file_type
#!/bin/bash
julien@ubuntu:/tmp$

```

In order to test your scripts, you will need to use this command: `chmod u+x file`. We will see later what does `chmod` mean and do, but you can have a look at `man chmod` if you are curious.

*Example*

```
julien@ubuntu:/tmp$ ls
12-file_type
lll
julien@ubuntu:/tmp$ ls -la lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ cat lll
#!/bin/bash
ls
julien@ubuntu:/tmp$ ls -l lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ chmod u+x lll # you do not have to understand this yet
julien@ubuntu:/tmp$ ls -l lll
-rwxrw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ ./lll
12-file_type
lll
julien@ubuntu:/tmp$

```

### Description

  Shell basic manipulation exercises are stored here

### Structure
 * 0-current_working-directory 
       prints the absolute path name of the current working directory.
 * 1-listit
           Display the contents list of your current directory.
 * 2-bring_me_home
          changes the working directory to the user’s home directory.
 * 3-listfiles
          Display current directory contents in a long format
 * 4-listmorefiles
          Display current directory contents, including hidden files 
 * 5-listfilesdigitonly
          Display current directory contents.
              *  Long format
              *  with user and group IDs displayed numerically
              *  And hidden files (starting with .)
 * 6-firstdirectory
           creates a directory named my_first_directory in the /tmp/ directory.
 * 7-movethatfile
           Move the file betty from /tmp/ to /tmp/my_first_directory.
 * 8-firstdelete : delete file betty
 * 9-firstdirdeletion : delete directory holberton in tmp directory
 * 10-back : changes working directory to previous one
 * 11-lists : list all files in the current directory, parent directory and he boot directory including hidden files in long format
 * 12-file_type : prints the type of the file iamfile in tmp directory
 * 13-symbolic_link : creates a symbolic link named __ls__ to /bin/ls
 * 14-copy_html : copies all HTML files from working to parent directory that does not exist
 * 15-lets_move : moves all files beginning with uppercase letter to tmp directory
 * 16-clean_emacs : deletes all files ending with "~" in working directory
 * 17-tree : creates series of directories
 * 18-commas : list files and directories of current directory ending with slash(/), sorted numerically and alphabetically, and include hidden files
