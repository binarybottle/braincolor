#! /bin/csh -fe
# 
# process.csh - process the files in the folder
#

set DATA = ( \
PeriSylvian.eps \
Dorsal-Ventral_surface1.eps \
Mid-Lateral_surface3.eps \
)

while ( $#DATA != 0 )
        set F = $DATA[1]
	set R = $F:r
	set E = $F:e

	echo recoloreps.py --mapFile ../parcLabels.xml \
		${R}_prepared.$E ${R}_recolored.$E 
	recoloreps.py --mapFile ../parcLabels.xml \
		${R}_prepared.$E ${R}_recolored.$E 

        shift DATA
end
