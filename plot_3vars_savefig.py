"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot, and saves it to a file named "myplot.png"

Inputs: the named file "sample_data_3vars.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt

plot_fname = "myplot.png"

fname = "combined_mflops_data.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df[var_names[0]].values.tolist()
dgemm_basic = df[var_names[1]].values.tolist()
dgemm_blass = df[var_names[2]].values.tolist()

plt.figure()

plt.title("MFLOPS Problem")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)

plt.plot(dgemm_basic, "r-o")
plt.plot(dgemm_blass, "b-x")

#plt.xscale("log")
#plt.yscale("log")

plt.xlabel("Problem Size")
plt.ylabel("MFLOPS/s")

varNames = [var_names[1], var_names[2]]
plt.legend(varNames, loc="best")

plt.grid(axis='both')

# save the figure before trying to show the plot
plt.savefig(plot_fname, dpi=300)


plt.show()

# EOF
