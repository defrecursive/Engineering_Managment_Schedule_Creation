import pandas as pd
import datetime
from calendar import month_name

data = pd.read_csv("Engineering_Management_-_New_Master_Sheet_-_Nabil_Hassan_-_Sheet8_1.csv")

month_names = list(month_name)[1:]
cohort_prefixes = ["Early", "Mid", "2nd Mid", "End", "2nd End"]
cohort_name = []

headers = data.columns
new_data = {}
for header in headers:
    new_data[header] = []

for month in month_names:
    if month in ["January", "May", "July", "October"]:
        for prefix in cohort_prefixes:
            cohort_name.append(prefix+"-"+month)
    else:
        for prefix in cohort_prefixes[:-1]:
            cohort_name.append(prefix+"-"+month)

COHORT_NAMES = data["cohort_one"]

cohort_month = []
cohort_year = []

for cohort in COHORT_NAMES:
    cohort_month.append(cohort[:-4])
    cohort_year.append(cohort[-4:])
    # print(cohort[:-4], cohort[-4:], sep="\t\t\t")


for name in cohort_name:
    for i in range(len(cohort_month)):
        if str(cohort_month[i]).strip() == name and str(cohort_year[i]).strip() == "2022":
            for header in headers:
                new_data[header].append(data[header][i])

print(len(new_data['cohort_one']))



# new_data = pd.DataFrame(new_data)
# new_data.to_csv("Output.csv")

# activity_filter = ['Orientation', 'Live Class', 'Review Class']
#
# ACTIVITY_TYPES = new_data['activity_type']
#
# refined_data = {}

# for header in headers:
#     refined_data[header] = []
#
# for ACTIVITY in ACTIVITY_TYPES:
#     if ACTIVITY in activity_filter:
#         index = ACTIVITY_TYPES.index(ACTIVITY)
#         for header in headers:
#             refined_data[header].append(new_data[header][index])

