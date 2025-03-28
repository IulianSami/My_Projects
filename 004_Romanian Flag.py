#4.   🟦🟨🟥  Romanian flag using Python:

import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots(figsize=(9, 5))

# Define the width of each stripe
stripe_width = 1 / 3

# Draw the blue stripe (left)
ax.fill_betweenx([0, 1], 0, stripe_width, color='#002B7F')  # Blue color

# Draw the yellow stripe (center)
ax.fill_betweenx([0, 1], stripe_width, 2 * stripe_width, color='#FCD116')  # Yellow color

# Draw the red stripe (right)
ax.fill_betweenx([0, 1], 2 * stripe_width, 1, color='#CE1126')  # Red color

# Set limits and remove axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Display the flag
plt.title("La multi ani Romania!", fontsize=15)
plt.show()