import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# 1.Load the cleaned dataset
# ==============================

df = pd.read_csv("vgsales_cleaned.csv")

# ==============================
# 2.Advanced EDA & Aggregations
# ==============================

# ==============================
# Top-selling genres based on global sales

# Grouping genres by sales

top_genre = df.groupby("Genre")["Global_Sales"].sum()

# Sort genres by global sales in descending order

top_genre_sorted = top_genre.sort_values(ascending=False)

# ********************* Display results *********************

print(top_genre_sorted)

# ==============================
# Correlation between sales regions and Critic Score

# Defining sales territories

sales = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]

# ********************* Display results *********************

for i in sales:
    correlation = df[i].corr(df["Critic_Score"])
    print(f"Correlation between {i} and Critic_Score : {correlation:.4f} ")

# ==============================
# Top-Platforms based on global sales

# Grouping platforms by sales

top_platform = df.groupby("Platform")["Global_Sales"].sum()

# Sort platforms by global sales in descending order

top_platform_sorted = top_platform.sort_values(ascending=False)

# ********************* Display results *********************

print(top_platform_sorted)

# ==============================
# View game information

# Retrieve game titles along with their global sales figures

search = df[df["Name"].str.contains(input("Put your game: "), case=False, regex=False)][["Name","Global_Sales"]]

# ********************* Display results *********************

if search.empty:
    print("No game found!")
else:
    print(f"The number of matching records for this game is {len(search)}\nThe total sales for matching records are {search['Global_Sales'].sum():.2f} million")



# ==============================
# 3.Data visualization
# ==============================

# ==============================
# Bar chart of the best-selling genres based on global sales

plt.bar(top_genre_sorted.index, top_genre_sorted.values, color="green", edgecolor="black")
plt.title("Genres by Global Sales", fontweight="bold", color="red")
plt.xlabel("Genres", fontstyle="italic")
plt.ylabel("Global Sales (million)", fontstyle="italic")

plt.tight_layout()
plt.show()

# ==============================
# Bar horizontal chart of the best-selling platforms based on global sales

plt.barh(top_platform_sorted.index, top_platform_sorted.values, color="blue", edgecolor="black")
plt.title("Platforms by Global Sales", fontweight="bold", color="red")
plt.xlabel("Global Sales (million)", fontstyle="italic")
plt.ylabel("Platforms", fontstyle="italic")

plt.tight_layout()
plt.show()

# ==============================
# Scatter plot of the relationship between sales regions and critic ratings

regions = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
for i in regions:
    plt.scatter(df[i], df["Critic_Score"], label= i, alpha=0.3, s=15, edgecolors="none")

plt.title("Regional Sales VS Critic Score", fontweight="bold", color="red")
plt.xlabel("Regional Sales (million)",fontweight="bold")
plt.ylabel("Critic Score", fontstyle="italic")

plt.legend()
plt.grid(alpha = 0.3)

plt.tight_layout()
plt.show()

# ==============================
# A complete plan for data visualization

figure, axes = plt.subplots(1, 3, figsize=(18, 6))

figure.suptitle("Video Game Sales Analysis Dashboard", fontsize=16, fontweight="bold")

axes[0].bar(top_genre_sorted.index, top_genre_sorted.values, color="green", edgecolor="black")
axes[0].set_title("Genres by Global Sales", fontweight="bold", color="red")
axes[0].set_xlabel("Genres", fontstyle="italic")
axes[0].set_ylabel("Global Sales (million)", fontstyle="italic")

axes[1].barh(top_platform_sorted.index, top_platform_sorted.values, color="blue", edgecolor="black")
axes[1].set_title("Platforms by Global Sales", fontweight="bold", color="red")
axes[1].set_xlabel("Global Sales (million)", fontstyle="italic")
axes[1].set_ylabel("Platforms", fontstyle="italic")

for i in regions:
    axes[2].scatter(df[i], df["Critic_Score"], label= i, alpha=0.3, s=15, edgecolors="none")
axes[2].set_title("Regional Sales VS Critic Score", fontweight="bold", color="red")
axes[2].set_xlabel("Regional Sales (million)",fontstyle="italic")
axes[2].set_ylabel("Critic Score", fontstyle="italic")

axes[2].legend()
axes[2].grid(alpha = 0.3)

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.savefig("video_games_dashboard.png", dpi=300, bbox_inches="tight")
plt.show()