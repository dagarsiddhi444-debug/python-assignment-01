# Name: Siddhi Dagar
# Roll No: 2501060046
# Course: BCA (AI & DS)
# Semester: 1st
# Subject: Problem Solving with Python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FNAME = "cleaned_pollution.csv"   # your file name


# ----------------------------------------
# Helper: show detected columns
# ----------------------------------------
def ask_map(cols):
    print("Columns found:", cols)
    print("If auto-detection fails, you will manually type column names.\n")


# ----------------------------------------
# Helper: auto-detect column names
# ----------------------------------------
def pick_column(cols, candidates):
    cols_lower = [c.lower() for c in cols]
    for cand in candidates:
        for i, name in enumerate(cols_lower):
            if cand in name:
                return cols[i]
    return None


# ----------------------------------------
# Main Program
# ----------------------------------------
def main():

    # Read CSV (no os/sys)
    try:
        df = pd.read_csv(FNAME, low_memory=False)
    except Exception:
        print(f"Could not read file: {FNAME}")
        return

    cols = list(df.columns)
    ask_map(cols)

    # Auto-detect columns
    date_col = pick_column(cols, ["date", "time", "timestamp"])
    pm25_col = pick_column(cols, ["pm2.5", "pm25", "pm_2_5", "pm2"])
    pm10_col = pick_column(cols, ["pm10", "pm_10"])
    aqi_col  = pick_column(cols, ["aqi", "air quality", "air_quality"])

    # Manual input if missing
    if date_col is None:
        date_col = input("Enter date/time column: ").strip()

    if pm25_col is None:
        pm25_col = input("Enter PM2.5 column (or leave blank): ").strip() or None

    if pm10_col is None:
        pm10_col = input("Enter PM10 column (or leave blank): ").strip() or None

    if aqi_col is None:
        aqi_col = input("Enter AQI column (or leave blank): ").strip() or None

    print("\nUsing:")
    print(" Date:", date_col)
    print(" PM2.5:", pm25_col)
    print(" PM10:", pm10_col)
    print(" AQI:", aqi_col)

    # Ensure date exists
    if date_col not in df.columns:
        print("ERROR: date column not found. Stopping.")
        return

    # Clean date column
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df = df.dropna(subset=[date_col]).sort_values(date_col).reset_index(drop=True)

    # Select existing columns
    selected_cols = [date_col]
    for c in (pm25_col, pm10_col, aqi_col):
        if c and c in df.columns:
            selected_cols.append(c)

    df = df[selected_cols].copy()

    # Convert pollutants to numeric + fill NaNs using numpy mean
    for c in selected_cols:
        if c == date_col:
            continue
        df[c] = pd.to_numeric(df[c], errors="coerce")
        mean_val = np.nanmean(df[c].values)
        if np.isnan(mean_val):
            print(f"Warning: column '{c}' has NO numeric values.")
        else:
            df[c] = df[c].fillna(mean_val)

    # Save cleaned data
    df.to_csv("cleaned_pollution.csv", index=False)
    print("Saved cleaned_pollution.csv")

    # ---------------------------------------------------
    # Plots
    # ---------------------------------------------------
    try:
        # AQI PLOT
        if aqi_col and aqi_col in df.columns:
            plt.figure(figsize=(10,4))
            plt.plot(df[date_col], df[aqi_col])
            plt.title("Daily AQI Trend")
            plt.xlabel("Date")
            plt.ylabel("AQI")
            plt.tight_layout()
            plt.savefig("aqi_trend.png")
            plt.close()
            print("Saved aqi_trend.png")

        # Monthly Average PM2.5
        if pm25_col and pm25_col in df.columns:
            df["Month"] = df[date_col].dt.to_period("M")
            monthly = df.groupby("Month")[pm25_col].mean()

            plt.figure(figsize=(10,4))
            monthly.index = monthly.index.astype(str)
            monthly.plot(kind="bar")

            plt.title("Monthly Avg PM2.5")
            plt.xlabel("Month")
            plt.ylabel("PM2.5")
            plt.tight_layout()
            plt.savefig("monthly_pm25.png")
            plt.close()
            print("Saved monthly_pm25.png")

        # Scatter plot
        if (pm25_col and pm10_col
            and pm25_col in df.columns
            and pm10_col in df.columns):

            plt.figure(figsize=(6,5))
            plt.scatter(df[pm25_col], df[pm10_col], s=10)
            plt.title("PM2.5 vs PM10")
            plt.xlabel("PM2.5")
            plt.ylabel("PM10")
            plt.tight_layout()
            plt.savefig("scatter_pm25_pm10.png")
            plt.close()
            print("Saved scatter_pm25_pm10.png")

    except Exception as e:
        print("Error while plotting:", e)

    # ---------------------------------------------------
    # Simple Text Report
    # ---------------------------------------------------
    with open("report.txt", "w") as f:
        f.write("Simple Air Quality Report\n")
        f.write("=========================\n")
        f.write(f"Rows after cleaning: {len(df)}\n\n")

        if pm25_col and pm25_col in df.columns:
            f.write(f"Mean PM2.5: {df[pm25_col].mean():.2f}\n")

        if pm10_col and pm10_col in df.columns:
            f.write(f"Mean PM10: {df[pm10_col].mean():.2f}\n")

        if aqi_col and aqi_col in df.columns:
            f.write(f"AQI Min/Max: {df[aqi_col].min():.2f} / {df[aqi_col].max():.2f}\n")

    print("Saved report.txt")
    print("Done!")


# Run program
if __name__ == "__main__":
    main()
