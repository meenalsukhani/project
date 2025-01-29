#In this Project ,I am  analyzing online education aspects and I have uploaded my data (udemy.csv) and i'll answer these Questions (i have answered these Questions in graphs' title only):
#1.	Which course categories (e.g., tech, business, arts) are the most popular?
#2.	Is there a correlation between course price and ratings?
#3.	What are the trends in student completion rates?
#4.	What factors affect students’ performance (e.g., study hours, age group)?
#5.	Which regions or demographics engage more in online learning?

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv("udemy.csv")
df.info()
df["content_duration"] = df["content_duration"].astype('int')
df.isnull().sum()

ax = sb.countplot(x="subject", data=df)
for bars in ax.containers:
  ax.bar_label(bars)
ax.set_title("Ans 1: tech category is the most popular as web dev is more in numbers")
plt.show() #ANS 1



df["ratings"] = (df["num_reviews"] / df["num_subscribers"]) * 100
# Calculate correlation (Pearson by default)
correlation = df['price'].corr(df['ratings'])

print(f"The correlation coefficient between column1 and column2 is: {correlation}")
#as correlation is close to 0, then it means that there is no correlaton b/w price and ratings
ax=sb.barplot(x="price",y='ratings',data=df)
ax.set_title("Ans 2: as correlation is close to 0, then it means that there is no correlaton b/w price and ratings")
plt.show() #ANS 2



# Convert published_timestamp to datetime
df["published_timestamp"] = pd.to_datetime(df["published_timestamp"])
# Calculate completion proxy
df["completion_proxy"] = (df["num_reviews"] / df["num_subscribers"]) * 100

# Analyze trends
completion_by_level = df.groupby("level")["completion_proxy"].mean()
completion_over_time = df.groupby(df["published_timestamp"].dt.year)["completion_proxy"].mean()
print("Completion Proxy by Course Level:\n", completion_by_level)
print("\nCompletion Proxy Trends Over Time:\n", completion_over_time)

# Completion Proxy by Level
completion_by_level.plot(kind="bar",title="Ans 3: Completion Proxy by Course Level",ylabel="Completion Proxy (%)")
plt.show() #ANS 3

# Completion Proxy Over Time
completion_over_time.plot(kind="line",marker="o",title="Ans 3: Completion Proxy Over Time",ylabel="Completion Proxy (%)")
plt.show() #ANS 3



# 1. Performance by Course Level
performance_by_level = df.groupby("level")["completion_proxy"].mean()

# 2. Performance by Price Range
df["price_range"] = pd.cut(df["price"],bins=[0, 50, 100, 150, 200],labels=["0-50", "51-100", "101-150", "151-200"])
performance_by_price = df.groupby("price_range")["completion_proxy"].mean()

# 3. Performance by Number of Lectures
performance_by_lectures = df.groupby("num_lectures")["completion_proxy"].mean()

# 4. Performance by Content Duration
performance_by_duration = df.groupby("content_duration")["completion_proxy"].mean()


# Performance by Level
performance_by_level.plot(kind="bar",title="Ans 4: Performance by Course Level",ylabel="Completion Proxy (%)")
plt.show() #ANS 4

# Performance by Price Range
performance_by_price.plot(kind="bar",title="Ans 4: Performance by Price Range",ylabel="Completion Proxy (%)")
plt.show() #ANS 4

# Performance by Number of Lectures
performance_by_lectures.plot(kind="line",marker="o",title="Ans 4: Performance by Number of Lectures",  ylabel="CompletionProxy (%)")
plt.show() #ANS 4

# Performance by Content Duration
performance_by_duration.plot(kind="line",marker="o",title="Ans 4: Performance by Content Duration",ylabel="Completion Proxy (%)")
plt.show() #ANS 4



ax = sb.countplot(x="is_paid", data=df)
ax.set_title("Ans 5: more people are engaged in paid courses")
plt.show() #ANS 5

ax = sb.countplot(x="level", data=df)
for bars in ax.containers:
  ax.bar_label(bars)
ax.set_title("Ans 5: more people are engaged in persuing course that is eligible for all levels")
plt.show() #ANS 5

sb.set(rc={"figure.figsize": (15, 5)})
ax = sb.countplot(x="content_duration", data=df)
for bars in ax.containers:
  ax.bar_label(bars)
ax.set_title("Ans 5: more people are engaged in 1 hr duration courses")
plt.show() #ANS 5

sb.set(rc={"figure.figsize": (15, 5)})
ax = sb.countplot(x="subject", data=df)
for bars in ax.containers:
  ax.bar_label(bars)
ax.set_title("Ans 5: more people are engaged in courses realted to web development")
plt.show() #ANS 5

sb.set(rc={"figure.figsize": (15, 5)})
ax = sb.countplot(x="price_range", data=df)
for bars in ax.containers:
  ax.bar_label(bars)
ax.set_title("Ans 5: more people are engaged in courses of price between 0-50")
plt.show() #ANS 5

