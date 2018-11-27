# Ovol2hexcodei_pitogether.py
# MIT LICENSE 2016
# Ying Xin

#Get the list of ParameterIndices of each Ovol2 hexcode.

def ovol2i_pitogether(j,allhexonly):
    # From all ParameterIndices, pick the ones with Ovol2 hexcode = 'i'
    ovol2i_pi = []
    for i in range(0, len(allhexonly)):
        if allhexonly[i] == j:
            ovol2i_pi.append(i)

    return ovol2i_pi