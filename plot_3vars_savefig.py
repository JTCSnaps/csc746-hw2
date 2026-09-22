"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads the combined Basic and blocked DGEMM data and saves a performance plot.

Inputs: the named file "combined_basic_blocked_mflops_data.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt

plot_fname = "basic_v_blocked.png"

fname = "combined_basic_blocked_mflops_data.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

# Split the data into the problem-size column and the five performance series.
# The blocked columns correspond to block sizes 2, 16, 32, and 64.

problem_sizes = df[var_names[0]].values.tolist()
basic = df[var_names[1]].values.tolist()
block_size_2 = df[var_names[2]].values.tolist()
block_size_16 = df[var_names[3]].values.tolist()
block_size_32 = df[var_names[4]].values.tolist()
block_size_64 = df[var_names[5]].values.tolist()




plt.figure()

plt.title("Basic vs Blocked DGEMM Performance")

# Use evenly spaced positions while displaying the exact problem-size labels.
xlocs = list(range(len(problem_sizes)))

plt.plot(xlocs, basic, "r-o", label=var_names[1])
plt.plot(xlocs, block_size_2, "b-x", label=var_names[2])
plt.plot(xlocs, block_size_16, "g-^", label=var_names[3])
plt.plot(xlocs, block_size_32, "m-s", label=var_names[4])
plt.plot(xlocs, block_size_64, "k-d", label=var_names[5])


#plt.xscale("log")
#plt.yscale("log")

plt.xticks(xlocs, problem_sizes)
plt.xlabel("Test Size")
plt.ylabel("MFLOP/s")
plt.legend(loc="best")

plt.grid(axis='both')

# save the figure before trying to show the plot
plt.savefig(plot_fname, dpi=300)


plt.show()

# EOF
