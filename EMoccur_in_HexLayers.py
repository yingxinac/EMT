# EMoccur_in_HexLayers.py
# MIT LICENSE 2016
# Ying Xin

#Get the number of parameter nodes with the occurrence of E/M state in each
# hexcode layer.

import DSGRN
import Data_added_GetParameterIndex as DGetParaIndex
import MorseList_to_ParaList
import Pitogether
getparameterindex_object = DGetParaIndex.Database.GetParameterIndex
database = DSGRN.Query.Database.Database("EMT_Ovol2notE.db") ###****** Choose
# the database
# file
# properly ******###

#Get the list of ParameterIndices with FP(0,0,*,*,*,2).
bounds002 = {"Zeb1":0,"Snail1":0,"Ovol2":2}
matches002 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(
    database, bounds002).matches()
print('Number of MorseGraphIndices with FP(0,0,*,*,*,2):')
print(len(matches002))
pilists_002 = MorseList_to_ParaList.MorseList_to_ParaList(matches002,
                                                         getparameterindex_object, database)
#Put the ParameterIndices together
P002_pitogether = Pitogether.pitogether(pilists_002)
print('Number of ParameterIndices with FP(0,0,*,*,*,2):')
print(len(P002_pitogether))


#Get the list of ParameterIndices with FP(3,3,*,*,*,0).
bounds330 = {"Zeb1":3,"Snail1":3,"Ovol2":0}
matches330 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(
    database, bounds330).matches()
print('Number of MorseGraphIndices with FP(3,3,*,*,*,0):')
print(len(matches330))
pilists_330 = MorseList_to_ParaList.MorseList_to_ParaList(matches330,
                                                         getparameterindex_object, database)
#Put the ParameterIndices together
P330_pitogether = Pitogether.pitogether(pilists_330)
print('Number of ParameterIndices with FP(3,3,*,*,*,0):')
print(len(P330_pitogether))


#Get the list of ParameterIndices of each hexcode layer.
import Ovol2HexcodeLayers
hexlayers = Ovol2HexcodeLayers.ovol2_layers ###****** Choose this according
#  to the databese file being used ******###

#-------------------------------------------------------------------------------
#Get the number of ParameterIndices with FP(0,0,*,*,*,
# 2) in each hexcode layer.
print('Number of ParameterIndices with FP(0,0,*,*,*,2) in each hexcode layer:')
P002_hexlayer = []
for i in range(0, len(hexlayers)):
    P002_hexlayer.append(len(set(hexlayers[i]) & set(P002_pitogether)))

print(P002_hexlayer)

#Get the number of ParameterIndices with FP(3,3,*,*,*,
# 0) in each hexcode layer.
print('Number of ParameterIndices with FP(3,3,*,*,*,0) in each hexcode layer:')
P330_hexlayer = []
for i in range(0, len(hexlayers)):
    P330_hexlayer.append(len(set(hexlayers[i]) & set(P330_pitogether)))

print(P330_hexlayer)