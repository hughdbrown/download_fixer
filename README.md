# Overview
Courses downloaded from the internet commonly have identical files repeated in directories.
These extra files eat up lots of space for no gains.

`download-fixer` modifies directories of identical files so that there is a single copy of
the file in a new directory and all directory-instances then point at the single copy.

# Installation
Run

    $ python setup.py install_scripts

from a command prompt. The installation will make a script file named `download-fixer` that you can run from the command line. On linux and OSX, the script will be placed in `/usr/local/bin`. I can't vouch for what happens in Windows.

# Operation
In a terminal, cd to the root directory of a collection of downloaded resources (video files,
PDFs, etc.). Run the script.

The script emits a sequence of shell operations that will effect the desired changes. You can either:

* redirect the script output to a file and run that from bash


    ```
    $ download-fixer.py > a.sh
    $ bash a.sh
    ```

* pipe the results of the script through bash

    ```
    $ download-fixer.py | bash
    ```

I  think that you should do the first for a couple of reasons. Most importantly, it gives you an
opportunity to review and edit the generated script. I think this is much safer. For example, what if your files have spaces and/or single quotes in the names -- does the script deal with this correctly? You won't know until it is too late if you pipe directly into bash.

A typical result will look like this:

```
#  ------------------------------ 3357a78cc88449316a4418b52b47738a712780e4
rm '04. Running_an_SQL_Group_By_with_MapReduce/MR-SQL-Joins.pdf
rm '05. A_MapReduce_Join_-_The_Map_Side/MR-SQL-Joins.pdf'
rm '06. A_MapReduce_Join_-_The_Reduce_Side/MR-SQL-Joins.pdf'
rm '07. A_MapReduce_Join_-_Sorting_and_Partitioning/MR-SQL-Joins.pdf'
rm '08. A_MapReduce_Join_-_Putting_it_all_together/MR-SQL-Joins.pdf'
mkdir -p data
mv '03. Running_an_SQL_Select_with_MapReduce/MR-SQL-Joins.pdf' 'data/3357a78cc88449316a4418b52b47738a712780e4-MR-SQL-Joins.pdf'
ln -s 'data/3357a78cc88449316a4418b52b47738a712780e4-MR-SQL-Joins.pdf' '03. Running_an_SQL_Select_with_MapReduce/MR-SQL-Joins.pdf'
ln -s 'data/3357a78cc88449316a4418b52b47738a712780e4-MR-SQL-Joins.pdf' '04. Running_an_SQL_Group_By_with_MapReduce/MR-SQL-Joins.pdf'
ln -s 'data/3357a78cc88449316a4418b52b47738a712780e4-MR-SQL-Joins.pdf' '05. A_MapReduce_Join_-_The_Map_Side/MR-SQL-Joins.pdf'
ln -s 'data/3357a78cc88449316a4418b52b47738a712780e4-MR-SQL-Joins.pdf' '06. A_MapReduce_Join_-_The_Reduce_Side/MR-SQL-Joins.pdf'
ln -s 'data/3357a78cc88449316a4418b52b47738a712780e4-MR-SQL-Joins.pdf' '07. A_MapReduce_Join_-_Sorting_and_Partitioning/MR-SQL-Joins.pdf'
ln -s 'data/3357a78cc88449316a4418b52b47738a712780e4-MR-SQL-Joins.pdf' '08. A_MapReduce_Join_-_Putting_it_all_together/MR-SQL-Joins.pdf'
#  ------------------------------
```

This takes the one duplicated file and places it in `data/` and then links the six copies to the single instance in this new storage directory.

# Limitations
1. All script operations on files quote file paths in single quotes. The code generated does not do the right thing if the file path has a single quote in it.
2. Identity is inferred by SHA1 hash. This means that collisions (and thus incorrect soft links) could be created if two files have the same hash. In practice, this only occurs if the two files are empty. This is another good reason to verify before running the script.

