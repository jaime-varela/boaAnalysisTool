# boaAnalysisTool
A simple gui tool to practice pyqt and pandas as well as analyze a BOA bank statement for anamolies and current subscriptions.


# How subscriptions are determined.

The program examines the description fields and groups the expenses according to pre-described algorithms (n-char match, number removal, etc.).  For each group the following is done:

1.) Determine if the signal is periodic.  If not, exit
2.) Determine the periodicity of the signal (weekly, monthly, daily, etc.)
3.) populate the periodic signal container (this is what is displayed on the table)