import matplotlib.pyplot as plt

# Data
categories = ['robust dispref. foc. words', 'marginal dispref. foc. words', 'tie', 'marginal pref. foc. words', 'robust pref. foc. words']
delve_initial = [6, 5, 1, 2, 1]
other_items = [3, 2, 1, 4, 5]

# Define pastel colors
colors = ['#F9665E', '#FF9797', '#EEF1E6', '#AFC7D0', '#799FCB']




# Bar plot
fig, ax = plt.subplots()
ax.bar("Delve-Initial Items", delve_initial[0], label=categories[0], color=colors[0])
ax.bar("Delve-Initial Items", delve_initial[1], bottom=delve_initial[0], label=categories[1], color=colors[1])
ax.bar("Delve-Initial Items", delve_initial[2], bottom=sum(delve_initial[:2]), label=categories[2], color=colors[2])
ax.bar("Delve-Initial Items", delve_initial[3], bottom=sum(delve_initial[:3]), label=categories[3], color=colors[3])
ax.bar("Delve-Initial Items", delve_initial[4], bot=sum(delve_initial[:4]), label=categories[4], color=colors[4])

ax.bar("Other Items", other_items[0], color=colors[0])
ax.bar("Other Items", other_items[1], bottom=other_items[0], color=colors[1])
ax.bar("Other Items", other_items[2], bottom=sum(other_items[:2]), color=colors[2])
ax.bar("Other Items", other_items[3], bottom=sum(other_items[:3]), color=colors[3])
ax.bar("Other Items", other_items[4], bottom=sum(other_items[:4]), color=colors[4])

# Y-axis limit and ticks
ax.set_ylim(0, 15)
ax.set_yticks([0, 5, 10, 15])

# Labels and title
ax.set_ylabel('Number of Items', fontsize=14)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], loc='lower left', fontsize=11)

# Increase fontsize of x ticks
ax.tick_params(axis='x', labelsize=12)  # Adjust the fontsize here

# Save plot
plt.savefig('/home/delve/results_and_visualisation/experimental_results.png')

# Display plot
plt.show()
