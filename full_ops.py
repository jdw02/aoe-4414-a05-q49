# full_ops.py

# Usage: py full_ops.py c_in n_wv
#  Python script to determine the output shape...
#  and operation count of an average pooling layer.

# Parameters:
#  c_in: input channel count
#  n_wv: number of weight vectors

# Output:
#  print(int(c_out)) # output channel count
#  print(int(h_out)) # output height count
#  print(int(w_out)) # output width count
#  print(int(adds))  # number of additions performed
#  print(int(muls))  # number of multiplications performed
#  print(int(divs))  # number of divisions performed

# Written by Jayden Warren

# import Python modules
import sys # argv
import math

# initialize script arguments
# initialize script arguments
c_in = float('nan')  # input channel count
n_wv = float('nan')  # number of weight vectors


# parse script arguments
if len(sys.argv)==3:
    c_in = float(sys.argv[1])  # input channel count
    n_wv = float(sys.argv[2])  # number of weight vectors
else:
    print(\
     'Usage: '\
     'py full_ops.py c_in n_wv'\
    )
    exit()

# write script below this line
c_out = n_wv
h_out = 1
w_out = 1
adds = n_wv*c_in
muls = n_wv*c_in
divs = 0

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed