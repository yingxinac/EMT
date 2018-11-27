Author: Ying Xin

These files compute data needed for Figures in "Some results from EMT data base query".

When switching to a different database, one needs to change the database file used in  "PointLayers.py" first, if the FP layers will be relevant later.

Then, when using
"ExactlyNstable.py",
"MonoEM_in_HexLayers.py",
"EMoccur_in_HexLayers.py",
"PlayersMono_in_HexLayers.py",
"Psoccur_in_HexLayers.py",
"Nstable_in_Hexlayers.py",
"Nstable_EM_in_Hexlayers.py" and
"Mono_at_FPs.py",
one needs to make modifications according to the database file being used.  Places in each scrpt where modifications need to be made are indicated with "###****** modifications ******###" at the end of those lines.  

For example, say we switch to the database file "Snail1notE.db", but used "Ovol2notE.db" before, then we just need to change all the "Ovol2" into "Snail1" in those lines.

Details on what each script does is inside those scripts.