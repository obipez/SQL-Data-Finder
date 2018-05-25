# SQL-Data-Finder
Project in exploring databases in PSQL, Python, Vagrant, through a virtual machine.


** Getting Started **
Instructions for running:
1. Download the database
2. Download vagrant and virtualbox
3. Start the virtual machine by 'vagrant up' then 'vagrant ssh'
4. Then use psql -d news -f newsdata.sql to setup the database
5. Then use the commands above for the views
6. CTRL + D to go back to the vagrant commandline
7. Use python3 news.py to get the results


** Prerequisites **
What things you need to install the software and how to install them.

-Vagrant:
    https://www.vagrantup.com/downloads.html
    
-VirtualBox:
    https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
    (Note: Have to download VirtualBox 5.1.30 in order to work with Vagrant)
    
-The Databased used:
    https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip    
