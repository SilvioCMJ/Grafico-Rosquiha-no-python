import myplotlib.pyplot as plt

fig, ax = plt.subplots()
circle = plt.Circle((0, 0), 0.64, color='white')
lbls = ['item1', 'item2', 'item3', 'item4']

ax.pie([7, 4, 2, 5], labels=lbls,autopct='%1.1f%%',pctdistance=.82)
ax.add_artist(circle)
ax.set_title("Grafico Rosquinha", fontsize=16)
plt.show()