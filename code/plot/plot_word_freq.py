"""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Increase global font size by 50%
plt.rcParams.update({'font.size': 21})  # 50% increase from 14 to 21

# First plot: Function Words
file_name_1 = 'plot_function_words'
file_path_1 = f'/home/delve/results_and_visualisation/{file_name_1}.tsv'
df1 = pd.read_csv(file_path_1, sep='\t')

# Pivot the table to have words as columns and years as rows
pivot_df1 = df1.pivot(index='year', columns='word', values='freq')

# Second plot: Baseline Words
file_name_2 = 'plot_baseline_words'
file_path_2 = f'/home/delve/results_and_visualisation/{file_name_2}.tsv'
df2 = pd.read_csv(file_path_2, sep='\t')

# Pivot the table to have words as columns and years as rows
pivot_df2 = df2.pivot(index='year', columns='word', values='freq')

# Create a figure with two subplots, one on top of the other
fig, axs = plt.subplots(2, 1, figsize=(16, 12))

# Plot the first data set
for word in pivot_df1.columns:
    axs[0].plot(pivot_df1.index, pivot_df1[word], label=word, linewidth=2.5)

#axs[0].set_xlabel('Year', fontsize=24)  # Increase from 16 to 24
axs[0].set_ylabel('Relative frequency', fontsize=24)  # Increase from 16 to 24
axs[0].set_title('Baseline Word Frequencies 1975-2024 (per million)', fontsize=27)  # Increase from 18 to 27
axs[0].set_xticks(np.arange(min(pivot_df1.index), max(pivot_df1.index) + 2, 5))
axs[0].legend(title='Words', loc='lower left', fontsize=24)  # Increase from 16 to 24
#axs[0].grid(True)

# Plot the second data set
for word in pivot_df2.columns:
    axs[1].plot(pivot_df2.index, pivot_df2[word], label=word, linewidth=2.5)

axs[1].set_xlabel('Year', fontsize=24)  # Increase from 16 to 24
axs[1].set_ylabel('Relative frequency', fontsize=24)  # Increase from 16 to 24
#axs[1].set_title('Baseline Word Frequencies 1975-2024 (per million)', fontsize=27)  # Increase from 18 to 27
axs[1].set_xticks(np.arange(min(pivot_df2.index), max(pivot_df2.index) + 2, 5))
axs[1].legend(title='Words', loc='lower left', fontsize=24)  # Increase from 16 to 24
axs[0].set_xticklabels([])
#axs[1].grid(True)

# Adjust the layout and save the figure
plt.tight_layout()
plt.savefig(f'/home/delve/results_and_visualisation/plot_combined_baseline.png')
plt.show()"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Increase global font size by 50%
plt.rcParams.update({'font.size': 21})  # 50% increase from 14 to 21

# Load data for the second plot: Baseline Words
file_name_2 = 'plot_baseline_words'
file_path_2 = f'/home/delve/results_and_visualisation/{file_name_2}.tsv'
df2 = pd.read_csv(file_path_2, sep='\t')

# Pivot the table to have words as columns and years as rows
pivot_df2 = df2.pivot(index='year', columns='word', values='freq')

# Create a figure with the desired aspect ratio
fig, ax = plt.subplots(figsize=(16, 6))

# Plot the second data set
for word in pivot_df2.columns:
    ax.plot(pivot_df2.index, pivot_df2[word], label=word, linewidth=2.5)

# Set axis labels, title, and legend
ax.set_xlabel('Year', fontsize=24)  # Increase from 16 to 24
ax.set_ylabel('Relative frequency', fontsize=24)  # Increase from 16 to 24
ax.set_title('Baseline Word Frequencies 1975-2024 (per million)', fontsize=27)  # Add plot title
ax.set_xticks(np.arange(min(pivot_df2.index), max(pivot_df2.index) + 2, 5))
ax.legend(title='Words', loc='lower left', fontsize=24)  # Increase from 16 to 24

# Adjust the layout and save the figure
plt.tight_layout()
plt.savefig(f'/home/delve/results_and_visualisation/plot_baseline_words.png')
plt.show()







import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Increase global font size by 50%
plt.rcParams.update({'font.size': 21})  # 50% increase from 14 to 21

# First plot: Function Words
file_name_1 = 'word_freqs_baseline_words_ai'
file_path_1 = f'/home/delve/results_and_visualisation/{file_name_1}.tsv'
df1 = pd.read_csv(file_path_1, sep='\t')

# Pivot the table to have words as columns and years as rows
pivot_df1 = df1.pivot(index='year', columns='word', values='freq')

# Second plot: Baseline Words
file_name_2 = 'word_freqs_baseline_words_ai2'
file_path_2 = f'/home/delve/results_and_visualisation/{file_name_2}.tsv'
df2 = pd.read_csv(file_path_2, sep='\t')

# Pivot the table to have words as columns and years as rows
pivot_df2 = df2.pivot(index='year', columns='word', values='freq')

# Create a figure with two subplots, one on top of the other
fig, axs = plt.subplots(2, 1, figsize=(16, 12))

# Plot the first data set
for word in pivot_df1.columns:
    axs[0].plot(pivot_df1.index, pivot_df1[word], label=word, linewidth=2.5)

#axs[0].set_xlabel('Year', fontsize=24)  # Increase from 16 to 24
axs[0].set_ylabel('Relative frequency', fontsize=24)  # Increase from 16 to 24
axs[0].set_title('Focal Word Frequencies 1975-2024 (per million)', fontsize=27)  # Increase from 18 to 27
axs[0].set_xticks(np.arange(min(pivot_df1.index), max(pivot_df1.index) + 2, 5))
axs[0].legend(title='Words', loc='lower left', fontsize=18)  # Increase from 16 to 24
#axs[0].grid(True)

# Plot the second data set
for word in pivot_df2.columns:
    axs[1].plot(pivot_df2.index, pivot_df2[word], label=word, linewidth=2.5)

axs[1].set_xlabel('Year', fontsize=24)  # Increase from 16 to 24
axs[1].set_ylabel('Relative frequency', fontsize=24)  # Increase from 16 to 24
#axs[1].set_title('Baseline Word Frequencies 1975-2024 (per million)', fontsize=27)  # Increase from 18 to 27
axs[1].set_xticks(np.arange(min(pivot_df2.index), max(pivot_df2.index) + 2, 5))
axs[1].legend(title='Words', loc='lower left', fontsize=18)  # Increase from 16 to 24
axs[0].set_xticklabels([])
#axs[1].grid(True)

# Adjust the layout and save the figure
plt.tight_layout()
plt.savefig(f'/home/delve/results_and_visualisation/plot_combined_ai.png')
plt.show()
