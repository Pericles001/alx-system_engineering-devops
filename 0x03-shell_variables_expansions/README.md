0x03. Shell, init files, variables and expansions
=================================================

-   By Julien Barbier
-   Ongoing project - started 08-24-2021, must end by 08-25-2021 (in about 21 hours) - you're done with 0% of tasks.
-   Checker will be released at 08-24-2021 12:00 PM
-   QA review fully automated.

About Bash projects
-------------------

Unless stated, all your projects will be auto-corrected with Ubuntu 14.04 LTS.

Resources
---------

**Read or watch**:

-   [Expansions](https://alx-intranet.hbtn.io/rltoken/oXnzBjLBA9t9dr7WuftdmQ "Expansions")
-   [Shell Arithmetic](https://alx-intranet.hbtn.io/rltoken/PLSUQnBcKKU5eEgRfRDlug "Shell Arithmetic")
-   [Variables](https://alx-intranet.hbtn.io/rltoken/SvdGNZJjKsPghzZEhaWu4Q "Variables")
-   [Shell initialization files](https://alx-intranet.hbtn.io/rltoken/tqud57kjsSYgDfeZDlwl3g "Shell initialization files")
-   [The alias Command](https://alx-intranet.hbtn.io/rltoken/zCemKQ8f1CxmODIs9dmcWg "The alias Command")
-   [Technical Writing](https://alx-intranet.hbtn.io/rltoken/gzXkaQsMeeNHSK3LbaKZeQ "Technical Writing")

**man or help**:

-   `printenv`
-   `set`
-   `unset`
-   `export`
-   `alias`
-   `unalias`
-   `.`
-   `source`
-   `printf`

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/RVM7z2LM2TRjYWc2IK0Rfw "explain to anyone"), **without the help of Google**:

### General

-   What happens when you type `$ ls -l *.txt`

### Shell Initialization Files

-   What are the `/etc/profile` file and the `/etc/profile.d` directory
-   What is the `~/.bashrc` file

### Variables

-   What is the difference between a local and a global variable
-   What is a reserved variable
-   How to create, update and delete shell variables
-   What are the roles of the following reserved variables: HOME, PATH, PS1
-   What are special parameters
-   What is the special parameter `$?`?

### Expansions

-   What is expansion and how to use them
-   What is the difference between single and double quotes and how to use them properly
-   How to do command substitution with `$()` and backticks

### Shell Arithmetic

-   How to perform arithmetic operations with the shell

### The `alias` Command

-   How to create an alias
-   How to list aliases
-   How to temporarily disable an alias

### Other `help` pages

-   How to execute commands from a file in the current shell

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your scripts will be tested on Ubuntu 20.04 LTS
-   All your scripts should be exactly two lines long (`$ wc -l file` should print 2)
-   All your files should end with a new line ([why?](http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
-   The first line of all your files should be exactly `#!/bin/bash`
-   A `README.md` file, at the root of the folder of the project, describing what each script is doing
-   You are not allowed to use `&&`, `||` or `;`
-   You are not allowed to use `bc`, `sed` or `awk`
-   All your files must be executable

More Info
---------

Read your `/etc/profile`, `/etc/inputrc` and `~/.bashrc` files.

Look at some files in the `/etc/profile.d` directory.

Note: You do not have to learn about `awk`, `tar`, `bzip2`, `date`, `scp`, `ulimit`, `umask`, or shell scripting, yet.

### Description
  Training on linux shell commands helping in  variable expansions

  This project is useful when it comes to review skills in shell usage to redirect between files

### Structure
 * 0-alias: creates an alias for the command rm *
 * 1-hello_you: prints hello [user name] to the terminal
 * 2-path: adds /action to PATH
 * 3-paths: counts the number of directories in PATH
 * 4-global_variables: lists environment vars
 * 5-local_variables: lists local vars
 * 6-create_local_variable: creates a local variable
 * 7-create_global_variable: creates a global variable
 * 8-true_knowledge: adds a number and a environment variable that holds a number
 * 9-divide_and_rule: divides two variables
 * 10-love_exponent_breath: exponentiates a variable with another variable
 * 11-binary_to_decimal: converts a variable from binary to decimal
 * 12-combinations: prints all the combinations from a-z except "oo"
 * 13-print_float: prints a number with 2 decimal points
 * 14-decimal_to_hexadecimal: converts a variable from decimal to hexadecimal
