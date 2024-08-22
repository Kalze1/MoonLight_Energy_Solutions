import pandas as pd
############ for benin-malanville
file_path = r'C:\Users\windows 10\Desktop\new\week_0\MoonLight_Energy_Solutions\data\benin-malanville.csv'
df = pd.read_csv(file_path)

numeric_df = df.select_dtypes(include='number')


summary_stats = numeric_df.describe().transpose()


summary_stats['median'] = numeric_df.median()
summary_stats['std'] = numeric_df.std()

print("******benin-malanville")
print(summary_stats)


summary_stats.to_csv('./data/benin_malanville_summary_statistics.csv')


####### for togo-dapaong_qc

file_path = r'C:\Users\windows 10\Desktop\new\week_0\MoonLight_Energy_Solutions\data\togo-dapaong_qc.csv'
df = pd.read_csv(file_path)

numeric_df = df.select_dtypes(include='number')


summary_stats = numeric_df.describe().transpose()


summary_stats['median'] = numeric_df.median()
summary_stats['std'] = numeric_df.std()

print("******togo-dapaong_qc")
print(summary_stats)


summary_stats.to_csv('./data/togo_dapaong_qc_summary_statistics.csv')


####### for sierraleone-bumbuna


file_path = r'C:\Users\windows 10\Desktop\new\week_0\MoonLight_Energy_Solutions\data\sierraleone-bumbuna.csv'
df = pd.read_csv(file_path)

numeric_df = df.select_dtypes(include='number')


summary_stats = numeric_df.describe().transpose()


summary_stats['median'] = numeric_df.median()
summary_stats['std'] = numeric_df.std()

print("******sierraleone-bumbuna")
print(summary_stats)


summary_stats.to_csv('./data/sierraleone_bumbuna_summary_statistics.csv')