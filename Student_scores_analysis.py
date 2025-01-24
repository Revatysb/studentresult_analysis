import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("student_scores.csv")
print(df.head())
print(df.describe())
print(df.info())
print(df.isnull().sum())

#DROP UNNAMED COLUMN
df=df.drop("Unnamed: 0",axis=1)
print(df.head())

#GENDER DISTRIBUTION
plt.figure(figsize=(5,5))
gender=sns.countplot(data=df,x="Gender")
gender.bar_label(gender.containers[0])
plt.title("GENDER DISTRIBUTION")
plt.show()
#From the above chart we have analysed that,"The number of females in the data is more than number of males"


#IMPACT OF PARENT'S EDUCATION ON DIFFERENT SCORES
different_scores=df.groupby("ParentEduc").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(different_scores)
plt.figure(figsize=(5,5))
sns.heatmap(different_scores,annot=True)
plt.title("RELATIONSHIP BETWEEN PARENT'S EDUCATION AND STUDENT'S SCORES")
plt.show()
#From the above chart we have concluded that the education of the parents have a good impact on the student's scores

#IMPACT OF PARENT'S MARITAL STATUS ON STUDENT'S SCORES
marital_status=df.groupby("ParentMaritalStatus").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(marital_status)
plt.figure(figsize=(5,5))
sns.heatmap(marital_status,annot=True)
plt.title("RELATIONSHIP BETWEEN PARENT'S MARITAL STATUS AND STUDENT'S SCORES")
plt.show()
#From the above chart we have concluded that there is no/negligible impact on the student's scores due to their parent's marital status

#COUNT OF STUDENTS BASED ON WEEKLY STUDY HOURS
study_hours_categories={"< 5":0,"5 - 10":0,"> 10":0}
for hours in df["WklyStudyHours"]:
    if hours=="< 5":
        study_hours_categories["< 5"]+=1
    elif hours=="5 - 10":
        study_hours_categories["5 - 10"]+=1
    elif hours=="> 10":
        study_hours_categories["> 10"]+=1
print("Students based on Weekly study hours:")
print(study_hours_categories)

#Understand how students distribute their study hours and access if more hours result in better performance

# Group the dataset by study hours and calculate average scores
study_hours_groups = df.groupby('WklyStudyHours')[['MathScore', 'ReadingScore', 'WritingScore']].mean().reset_index()

# Plot using Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(data=study_hours_groups, x='WklyStudyHours', y='MathScore', label='Math Score',marker='o')
sns.lineplot(data=study_hours_groups, x='WklyStudyHours', y='ReadingScore', label='Reading Score', marker='o')
sns.lineplot(data=study_hours_groups, x='WklyStudyHours', y='WritingScore', label='Writing Score', marker='o')

# Adding titles and labels
plt.title('Average Scores by Weekly Study Hours', fontsize=16)
plt.xlabel('Weekly Study Hours', fontsize=12)
plt.ylabel('Average Score', fontsize=12)
plt.legend(title='Subjects')
plt.grid(True)

# Show plot
plt.show()
#Clear trends showing how scores increase as study hours increase

#IMPACT OF SIBLINGS ON STUDY HOURS
sns.boxplot(data=df,x="NrSiblings",y="WklyStudyHours", hue="WklyStudyHours",legend=False,palette="muted")
plt.title("Weekly study hours by Number of Siblings",fontsize=16)
plt.xlabel('Number of siblings', fontsize=12)
plt.ylabel('Weekly Study Hours', fontsize=12)
plt.show()

#DISTRIBUTION OF ETHNIC GROUPS
print(df["EthnicGroup"].unique())
groupA=df.loc[(df["EthnicGroup"]=="group A")].count()
groupB=df.loc[(df["EthnicGroup"]=="group B")].count()
groupC=df.loc[(df["EthnicGroup"]=="group C")].count()
groupD=df.loc[(df["EthnicGroup"]=="group D")].count()
groupE=df.loc[(df["EthnicGroup"]=="group E")].count()

label_name=["group A","group B","group C","group D","group E"]
ethnic_list=[groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
plt.pie(ethnic_list,labels=label_name,autopct="%1.2f%%")
plt.title("Distribution of ethnic groups")
plt.show()

#Performance Distribution by Transportation Means
sns.violinplot(data=df,x='TransportMeans',y="ReadingScore" , palette='Set2')
plt.title('Reading Performance Distribution by Transportation Means')
plt.show()
sns.violinplot(data=df,x='TransportMeans',y="WritingScore" , palette='Set2')
plt.title('Writing Performance Distribution by Transportation Means')
plt.show()
sns.violinplot(data=df,x='TransportMeans',y="MathScore" , palette='Set2')
plt.title('Math Performance Distribution by Transportation Means')
plt.show()
#From the above charts, Transportation Means have negligible effect on Performance 

# Define outstanding performance
top_students = df[(df['MathScore'] > 90) & (df['ReadingScore'] > 90) & (df['WritingScore'] > 90)]
print("Top-Performing Students:")
print(top_students)

#Lunch Type Distribution by Parental Education
sns.countplot(data=df, x='ParentEduc', hue='LunchType', palette='viridis')
plt.title('Lunch Type Distribution by Parental Education')
plt.xticks(rotation=45)
plt.show()
