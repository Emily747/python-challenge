#Emily Hudson
#Homerwork 3 Python Challenge
#DVA Cohort 3

import pandas as pd
file = "PyPoll_data.csv"

pypoll_df = pd.read_csv(file)

votes_cast = pypoll_df["Voter ID"].count()

pypoll_df["Candidate"].unique()

counts = pypoll_df["Candidate"].value_counts()

counts_df = pd.DataFrame(counts)

counts_df["Percentage"] = (counts_df["Candidate"]/3521001)*100
div = "--------------------------------"
counts_df["Percentage"] = counts_df["Percentage"].astype(float).map("{:,.0f}%".format)

counts_df = counts_df.rename(columns={"Candidate": "Total Votes"})

import sys
sys.stdout = open('Election Results.txt', 'w')
print("Election Results")
print(div)
print(f"Total Votes: {votes_cast}")
print(div)
print(counts_df)
print(div)
print("Winner: Khan")
print(div)

sys.stdout.close()