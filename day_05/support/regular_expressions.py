import re

line = "SBATCH: start at 12h08h23 on milou1"
start_time = re.findall('^SBATCH: start at (.+) on .+$', line)
print start_time

line = "<Iteration_query-def>HV2D61Y02HIG62 length=399 xy=2963_3068 region=2 run=R_2012_10_10_07_10_03_</Iteration_query-def>"
result = re.findall("<Iteration_query-def>(.+)</Iteration_query-def>", line)
print result

line = ">centroid=MISEQ:39:000000000-A3WH1:1:1101:19758:3096:GCCAAT;seqs=1;size=12;"
result = re.findall("size=([0-9]+)", line)
print result

">centroid=MISEQ:39:000000000-A3WH1:1:1101:19758:3096:GCCAAT;seqs=1;size=12;", ">centroid=MISEQ:39:000000000-A3WH1:1:1101:19758:3096:GCCAAT;seqs=1;size=98;", ">centroid=MISEQ:39:000000000-A3WH1:1:1101:19758:3096:GCCAAT;seqs=1;size=0;"