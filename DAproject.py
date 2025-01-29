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

df["ratings"] = (df["num_reviews"] / df["num_subscribers"]) * 100
# Calculate correlation (Pearson by default)
correlation = df['price'].corr(df['ratings'])

print(
    f"The correlation coefficient between column1 and column2 is: {correlation}"
)
#as correlation is close to 0, then it means that there is no correlaton b/w price and ratings

# Convert published_timestamp to datetime
df["published_timestamp"] = pd.to_datetime(df["published_timestamp"])

# Calculate completion proxy
df["completion_proxy"] = (df["num_reviews"] / df["num_subscribers"]) * 100

# Analyze trends
completion_by_level = df.groupby("level")["completion_proxy"].mean()
completion_over_time = df.groupby(
    df["published_timestamp"].dt.year)["completion_proxy"].mean()

print("Completion Proxy by Course Level:\n", completion_by_level)
print("\nCompletion Proxy Trends Over Time:\n", completion_over_time)

# Completion Proxy by Level
completion_by_level.plot(kind="bar",
                         title="Completion Proxy by Course Level",
                         ylabel="Completion Proxy (%)")
plt.show()

# Completion Proxy Over Time
completion_over_time.plot(kind="line",
                          marker="o",
                          title="Completion Proxy Over Time",
                          ylabel="Completion Proxy (%)")
plt.show()

# 1. Performance by Course Level
performance_by_level = df.groupby("level")["completion_proxy"].mean()

# 2. Performance by Price Range
df["price_range"] = pd.cut(df["price"],
                           bins=[0, 50, 100, 150, 200],
                           labels=["0-50", "51-100", "101-150", "151-200"])
performance_by_price = df.groupby("price_range")["completion_proxy"].mean()

# 3. Performance by Number of Lectures
performance_by_lectures = df.groupby("num_lectures")["completion_proxy"].mean()

# 4. Performance by Content Duration
performance_by_duration = df.groupby(
    "content_duration")["completion_proxy"].mean()

# Print results
print("Performance by Course Level:\n", performance_by_level)
print("\nPerformance by Price Range:\n", performance_by_price)
print("\nPerformance by Number of Lectures:\n", performance_by_lectures)
print("\nPerformance by Content Duration:\n", performance_by_duration)

# Performance by Level
performance_by_level.plot(kind="bar",
                          title="Performance by Course Level",
                          ylabel="Completion Proxy (%)")
plt.show()

# Performance by Price Range
performance_by_price.plot(kind="bar",
                          title="Performance by Price Range",
                          ylabel="Completion Proxy (%)")
plt.show()

# Performance by Number of Lectures
performance_by_lectures.plot(kind="line",
                             marker="o",
                             title="Performance by Number of Lectures",
                             ylabel="Completion Proxy (%)")
plt.show()

# Performance by Content Duration
performance_by_duration.plot(kind="line",
                             marker="o",
                             title="Performance by Content Duration",
                             ylabel="Completion Proxy (%)")
plt.show()

ax = sb.countplot(x="is_paid", data=df)

#more people are engaged in paid courses

ax = sb.countplot(x="level", data=df)
for bars in ax.containers:
  ax.bar_label(bars)

#more people are engaged in persuing course that is eligible for all levels

sb.set(rc={"figure.figsize": (15, 5)})
ax = sb.countplot(x="content_duration", data=df)
for bars in ax.containers:
  ax.bar_label(bars)

#more people are engaged in 1 hr duration courses

sb.set(rc={"figure.figsize": (15, 5)})
ax = sb.countplot(x="subject", data=df)
for bars in ax.containers:
  ax.bar_label(bars)

#more people are engaged in courses realted to web development

sb.set(rc={"figure.figsize": (15, 5)})
ax = sb.countplot(x="price_range", data=df)
for bars in ax.containers:
  ax.bar_label(bars)

#more people are engaged in courses of price between 0-50
