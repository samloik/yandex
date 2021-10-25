
import sys

Rn = { }

oSum = {}


def find_min_R(min, max):
	if min < max:
		if Rn[min] < Rn[max]:
			if Rn[max-1] < Rn[max]:
				find_min_R(min, max - 1)
				oSum[max] = oSum[max-1] + 500
				return
			elif Rn[max-1] == Rn[max]:
				find_min_R(min, max-1)
				oSum[max] = oSum[max-1]
				return
			else:
				find_min_R(min, max-1)
				oSum[max] = oSum[max-1] - 500
				return
		elif Rn[min] > Rn[max]:
			if Rn[min] > Rn[min+1]:
				find_min_R(min+1, max)
				oSum[min] = oSum[min+1] + 500
				return
			elif Rn[min] == Rn[min+1]:
				find_min_R(min+1, max)
				oSum[min] = oSum[min+1]
				return
			else:
				find_min_R(min+1, max)
				oSum[min] = oSum[min+1]- 500
				return
		else:
			find_min_R(min + 1, max)
			oSum[min] = oSum[min+1]
			return
	else:
		oSum[min] = 500
		return





j = input().split()

Rmin = 0
Rmax = int(j[0])


for N in range(Rmax):
	Rn[N] = input().split()

for i in range(Rmax):
	oSum[i] = 0

find_min_R(Rmin,Rmax-1)

print( sum(oSum.values()) )


