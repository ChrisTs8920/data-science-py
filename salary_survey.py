import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file_path = os.path.join(os.path.dirname(__file__), "er.csv")
s = pd.read_csv(file_path)

# Programming Languages stats
col1 = s["Με ποιες γλώσσες προγραμματισμού δουλεύεις επαγγελματικά αυτή την περίοδο;"]

jscount = 0
phpcount = 0
pycount = 0
Cscount = 0
Javacount = 0
C_cppcount = 0

for i in s.index:
    if "JavaScript" in col1[i]:
        jscount += 1
    elif "PHP" in col1[i]:
        phpcount += 1
    elif "Python" in col1[i]:
        pycount += 1
    elif "C#" in col1[i]:
        Cscount += 1
    elif "Java" in col1[i]:
        Javacount += 1
    elif "C" in col1[i] or "C++" in col1[i]:
        C_cppcount += 1

df1 = pd.DataFrame(
    {
        "JavaScript": [jscount],
        "PHP": [phpcount],
        "Python": [pycount],
        "C#": [Cscount],
        "Java": [Javacount],
        "C/C++": [C_cppcount],
    }
)


# education stats
col2 = s["Ποιό είναι το επίπεδο σπουδών σου;"]

lcount = 0  # lukeio count
icount = 0  # IEK count
bcount = 0  # Bachelor's count
mcount = 0  # Master's count
pcount = 0  # PhD count
ocount = 0  # Other count

for i in s.index:
    if col2[i] == "IEK":
        icount += 1
    elif col2[i] == "Λύκειο":
        lcount += 1
    elif col2[i] == "Bachelor's":
        bcount += 1
    elif col2[i] == "Master":
        mcount += 1
    elif col2[i] == "PhD":
        pcount += 1
    else:
        ocount += 1

df2 = pd.DataFrame(
    {
        "High School": [lcount],
        "Ι.Ε.Κ.": [icount],
        "Bachelors": [bcount],
        "Master": [mcount],
        "PhD": [pcount],
        "Other": [ocount],
    }
)

# remote stats
col3 = s["Ποιος είναι ο τρόπος εργασίας;"]

bothcount = 0  # both
remcount = 0  # remote
nocount = 0  # on-site

for i in s.index:
    if col3[i] == "Και τα δύο":
        bothcount += 1
    elif col3[i] == "Απομακρυσμένα":
        remcount += 1
    elif col3[i] == "Στον χώρο του εργοδότη":
        nocount += 1

df3 = pd.DataFrame(
    {
        "Both": [bothcount],
        "Remote": [remcount],
        "On-site": [nocount],
    }
)

# Athens stats
col4 = s["Σε ποια πόλη δουλεύεις;"]

Acount = 0
wage_median = 0

for i in s.index:
    if col4[i] == "Αθήνα":
        Acount += 1

wage_median = s["Ποιος είναι ο ΕΤΗΣΙΟΣ ΚΑΘΑΡΟΣ μισθός σου σε €;"].median()

df4 = pd.DataFrame(
    {
        "How many": [Acount],
        "Wage Median": [wage_median],
        "Median Monthly": [wage_median / 14],
    }
)

# plots
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))

p1 = df1.plot(kind="bar", title="Programming Languages", ax=ax[0][0])
for i in range(6):
    p1.bar_label(p1.containers[i])

p2 = df2.plot(kind="bar", title="Education level", ax=ax[0][1])
for i in range(6):
    p2.bar_label(p2.containers[i])

p3 = df3.plot(kind="bar", title="Remote work", ax=ax[1][0])
for i in range(3):
    p3.bar_label(p3.containers[i])

p4 = df4.plot(kind="bar", title="From Athens", ax=ax[1][1])
for i in range(3):
    p4.bar_label(p4.containers[i])


if __name__ == "__main__":
    plt.show()
