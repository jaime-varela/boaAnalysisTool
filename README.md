# boaAnalysisTool
A simple gui tool to practice pyqt and pandas as well as analyze a BOA bank statement and current subscriptions.

At some point I want to add anomaly detection as well.

# Query view

Allows you to load your bank statement files and perform regex queries:

![Query Main View](./readmeResources/queryMainView.png)


# How subscriptions are determined.

The program examines the description fields and groups the expenses according to pre-described algorithms (n-char match, number removal, etc.).  For each group the following is done:

1.) Determine if the signal is scheduled.  If not, exit
2.) Determine the periodicity of the signal (weekly, monthly, daily, etc.)
3.) populate the periodic signal container (this is what is displayed on the table)

A user can change the settings of the grouping algorithms in the right side panel.

![Schedule Main View](./readmeResources/scheduleMainView.png)

The system isn't perfect and requires more work.  For example in the above schedule there is an issue with an expense that has both debits and credits with a similar name and results in a weird daily deposit (the fully blacked out entry.  Entries have been blacked out to removed personal information).

For strange expenses the query window can be used.  At some point I will make the table clickable to jump to the set of expenses associated with each entry.


# Running and using the program

For the dependencies:

```
pip install -r requirements.txt
```

For the scheduler run the following (using python3):

```
python schedulewindow.py 
```

for the query window

```
python querywindow.py 
```

For each application use the "File->Load" button on the top left to find and load your bank statement.


You may have to run:

```
sudo apt install --reinstall qt5-default qttools5* pyqt5-dev-tools libqt5* qt5-* qtbase5-* qtcreator build-essential qtdeclarative5* libqt5webkit5* mesa-common-* libglu1-mesa-* qtbase5-dev
```
on linux systems to get the dependencies right.
# Libraries in use

1.) pandas

2.) numpy

3.) scipy

4.) levenstein

