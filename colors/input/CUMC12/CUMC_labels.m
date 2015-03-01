% (0) means label not included in mensh_s01 (atlas) 
% If there is a 0 in the 2nd column, the label is not included in mindboggle

Labels = [0;    %      Left  Cerebral Exterior    (0) Left Cerebral Exterior          
0;    %      Right Cerebral Exterior         (0) Right Cerebral Exterior         
3;    %      Left  Cerebellum Exterior       Left Cerebellum Exterior                
4;    %      Right Cerebellum Exterior       Right Cerebellum Exterior               
5;    %      Left  Cerebral White Matter     Left Cerebral White Matter              
6;    %      Right Cerebral White Matter     Right Cerebral White Matter             
7;    %      Left  Cerebellum White Matter   Left Cerebellum White Matter            
8;    %      Right Cerebellum White Matter   Right Cerebellum White Matter           
9;    %      Left  Lateral Ventricle         Left Lateral Ventricle          
10;    %      Right Lateral Ventricle         Right Lateral Ventricle         
11;    %      4th Ventricle                   4th Ventricle           
12;    %      Brain Stem                      Brain Stem              
13;    %      Left  Inf Lat Vent              Left Inf Lat Vent               
14;    %      Right Inf Lat Vent              Right Inf Lat Vent              
15;    %      Left  Hippocampus               Left Hippocampus
16;    %      Right Hippocampus               Right Hippocampus
17;    %      Left  Thalamus Proper           Left Thalamus Proper
18;    %      Right Thalamus Proper           Right Thalamus Proper
19;    %      Left  VentralDC                 Left VentralDC
20;    %      Right VentralDC                 Right VentralDC
21;    %      3rd Ventricle                   3rd Ventricle
22;    %      CSF                             CSF
23;    %      Left Caudate                    Left Caudate
24;    %      Right Caudate                   Right Caudate
25;    %      Left Putamen                    Left Putamen
26;    %      Right Putamen                   Right Putamen
27;    %      Left Pallidum                   Left Pallidum
28;    %      Right Pallidum                  Right Pallidum
29;    %      Left Amygdala                   Left Amygdala
30;    %      Right Amygdala                  Right Amygdala
31;    %      Left vessel                     Left vessel     
32;    %      Right vessel                    Right vessel    
33;    %      Left Accumbens area             Left Accumbens area     
34;    %      Right Accumbens area            Right Accumbens area    
35;    %      Left OP                         L Occipital Pole        o
36;    %      Right OP                        R Occipital Pole        o
37;    %      Left CN                         L Cuneal Cortex o
38;    %      Right CN                        R Cuneal Cortex o
39;    %      Left OLs                        "L Lateral Occipital Cortex, superior"  o
40;    %      Right OLs                       "R Lateral Occipital Cortex, superior"  o
41;    %      Left SCLC                       L Supracalcarine Cortex p @rno
42;    %      Right SCLC                      R Supracalcarine Cortex p @rno
43;    %      Left CALC                       L Intracalcarine Cortex p @rno
44;    %      Right CALC                      R Intracalcarine Cortex p @rno
45;    %      Left OLi                        "L Lateral Occipital Cortex, inferior"  o
46;    %      Right OLi                       "R Lateral Occipital Cortex, inferior"  o
47;    %      Left OF                         L Occipital Fusiform Gyrus      o
48;    %      Right OF                        R Occipital Fusiform Gyrus      o
49;    %      Left LG                         L Lingual Gyrus o           (*extends into OL)
50;    %      Right LG                        R Lingual Gyrus o           (*extends into OL)
51;    %      Left PCN                        L Precuneous Cortex  p @rno (*extends into OL)
52;    %      Right PCN                       R Precuneous Cortex  p @rno (*extends into OL)
53;    %      Left AG                         L Angular Gyrus p
54;    %      Right AG                        R Angular Gyrus p
55;    %      Left SPL                        L Superior Parietal Lobule      p
56;    %      Right SPL                       R Superior Parietal Lobule      p
57;    %      Left TO2                        "L Middle Temporal Gyrus, temporooccipital part"        t
58;    %      Right TO2                       "R Middle Temporal Gyrus, temporooccipital part"        t
59;    %      Left TOF                        L Temporal Occipital Fusiform Cortex    t
60;    %      Right TOF                       R Temporal Occipital Fusiform Cortex    t
61;    %      Left TO3                        "L Inferior Temporal Gyrus, temporooccipital part"      t
62;    %      Right TO3                       "R Inferior Temporal Gyrus, temporooccipital part"      t
63;    %      Left POG                        L Postcentral Gyrus     p       
64;    %      Right POG                       R Postcentral Gyrus     p       
65;    %      Left SGp                        "L Supramarginal Gyrus, posterior"      p       
66;    %      Right SGp                       "R Supramarginal Gyrus, posterior"      p       
67;    %      Left CGp                        "L Cingulate Gyrus, posterior"  p       MedialParalimbic
68;    %      Right CGp                       "R Cingulate Gyrus, posterior"  p       MedialParalimbic
69;    %      Left PRG                        L Precentral Gyrus      f       
70;    %      Right PRG                       R Precental Gyrus       f       
71;    %      Left SGa                        "L Supramarginal Gyrus, anterior"       p       
72;    %      Right SGa                       "R Supramarginal Gyrus, anterior"       p       
73;    %      Left PO                         L Parietal Operculum Cortex     p       Intrasylvian
74;    %      Right PO                        R Parietal Operculum Cortex     p       Intrasylvian
75;    %      Left PT                         L Planum Temporale t       Intrasylvian @rno
76;    %      Right PT                        R Planum Temporale      t       Intrasylvian @rno
77;    %      Left T1p                        "L Superior Temporal Gyrus, posterior"  t       
78;    %      Right T1p                       "R Superior Temporal Gyrus, posterior"  t       
79;    %      Left T2p                        "L Middle Temporal Gyrus, posterior"    t       
80;    %      Right T2p                       "R Middle Temporal Gyrus, posterior"    t       
81;    %      Left PHp                        "L Parahippocampal Gyrus, posterior"    t       MedialParalimbic
82;    %      Right PHp                       "R Parahippocampal Gyrus, posterior"    t       MedialParalimbic
83;    %      Left TFp                        "L Temporal Frontal Cortex, posterior"  t       
84;    %      Right TFp                       "R Temporal Frontal Cortex, posterior"  t       
85;    %      Left T3p                        "L Inferior Temporal Gyrus, posterior"  t       
86;    %      Right T3p                       "R Inferior Temporal Gyrus, posterior"  t       
87;    %      Left INS                        L Insular Cortex        t       Intrasylvian
88;    %      Right INS                       R Insular Cortex        t       Intrasylvian
89;    %      Left  H1                        L Heschl's Gyrus        t       Intrasylvian
90;    %      Right H1                        R Heschl's Gyrus        t       Intrasylvian
91;    %      Left  PP                        L Planum Polare t       Intrasylvian
92;    %      Right PP                        R Planum Polare t       Intrasylvian
93;    %      Left  CO                        L Central Opercular Cortex      f       Intrasylvian
94;    %      Right CO                        R Central Opercular Cortex      f       Intrasylvian
95;    %      Left  PHa                       "L Parahippocampal Gyrus, anterior"     t       MedialParalimbic
96;    %      Right PHa                       "R Parahippocampal Gyrus, anterior"     t       MedialParalimbic
97;    %      Left  F1                        L Superior Frontal Gyrus        f       "PFC,DLPFC"
98;    %      Right F1                        R Superior Frontal Gyrus        f       "PFC,DLPFC"
99;    %      Left  SMC                       L Supplementary Motor Cortex    f       
100;    %      Right SMC                       R Supplementary Motor Cortex    f       
101;    %      Left  CGa                       "L Cingulate Gyrus, anterior"   f       MedialParalimbic
102;    %      Right CGa                       "R Cingulate Gyrus, anterior"   f       MedialParalimbic
103;    %      Left  T1a                       "L Superior Temporal Gyrus, anterior"   t       
104;    %      Right T1a                       "R Superior Temporal Gyrus, anterior"   t       
105;    %      Left  T2a                       "L Middle Temporal Gyrus, anterior"     t       
106;    %      Right T2a                       "R Middle Temporal Gyrus, anterior"     t       
107;    %      Left  TFa                        "L Temporal Frontal Cortex, anterior"   t       
108;    %      Right TFa                       "R Temporal Frontal Cortex, anterior"   t       
109;    %      Left  T3a                       "L Inferior Temporal Gyrus, anterior"   t       
110;    %      Right T3a                       "R Interior Temporal Gyrus, anterior"   t       
111;    %      Left  F2                        L Middle Frontal Gyrus  f       "PFC,DLPFC"
112;    %      Right F2                        R Middle Frontal Gyrus  f       "PFC,DLPFC"
113;    %      Left  BFsbcmp                    L Basal Forebrain       t       
114;    %      Right BFsbcmp                   R Basal Forebrain       t       
115;    %      Left  PAC                        L Paracingulate Gyrus   f       MedialParalimbic
116;    %      Right PAC                       R Paracingulate Gyrus   f       MedialParalimbic
117;    %      Left  F3o                        "L Inferior Frontal Gyrus, pars opercularis"    f       
118;    %      Right F3o                       "R Interior Frontal Gyrus, pars opercularis"    f       
119;    %      Left  FO                         L Frontal Operculum Cortex      f       Intrasylvian
120;    %      Right FO                        R Frontal Operculum Cortex      f       Intrasylvian
121;    %      Left  TP                         L Temporal Pole t       
122;    %      Right TP                        R Temporal Pole t       
123;    %      Left  SC                         L Subcallosal Cortex    f       MedialParalimbic
124;    %      Right SC                        R Subcallosal Cortex    f       MedialParalimbic
125;    %      Left  FOC                        L Frontal Orbital Cortex        f       PFC
126;    %      Right FOC                       R Frontal Orbital Cortex        f       PFC
127;    %      Left  F3t                        "L Inferior Frontal Gyrus, pars triangularis"   f       PFC
128;    %      Right F3t                       "R Inferior Frontal Gyrus, pars triangularis"   f       PFC
129;    %      Left  FMC                        L Frontal Medial Cortex f       PFC
130;    %      Right FMC                       R Frontal Medial Cortex f       PFC
131;    %      Left  FP                         L Frontal Pole  f       PFC
132];    %      Right FP                        R Frontal Pole  f       PFC

Names = {'L cerebral exterior';          
'R cerebral exterior';         
'L cerebellum exterior';                
'R cerebellum exterior';               
'L cerebral white matter';              
'R cerebral white matter';             
'L cerebellum white matter';            
'R cerebellum white matter';           
'L lateral ventricle';          
'R lateral ventricle';         
'4th ventricle';           
'brainstem';              
'L inf. lateral ventricle';               
'R inf. lateral ventricle';              
'L hippocampus';
'R hippocampus';
'L thalamus proper';
'R thalamus proper';
'L ventralDC';
'R ventralDC';
'3rd ventricle';
'CSF';
'L caudate';
'R caudate';
'L putamen';
'R putamen';
'L pallidum';
'R pallidum';
'L amygdala';
'R amygdala';
'L vessel';
'R vessel';    
'L accumbens area';     
'R accumbens area';    
'L occipital pole';
'R occipital pole';
'L cuneal cortex';
'R cuneal cortex';
'L lateral occipital cortex, sup.';
'R lateral occipital cortex, sup.';
'L supracalcarine cortex';
'R supracalcarine cortex';
'L Intracalcarine cortex';
'R Intracalcarine cortex';
'L lateral occipital cortex, inf.';
'R lateral occipital cortex, inf.';
'L occipital fusiform gyrus';
'R occipital fusiform gyrus';
'L lingual gyrus';
'R lingual gyrus';
'L precuneous cortex';
'R precuneous cortex';
'L angular gyrus';
'R angular gyrus';
'L sup. parietal lobule';
'R sup. parietal lobule';
'L middle temporal gyrus (temporooccipital)';
'R middle temporal gyrus (temporooccipital)';
'L temporal occipital fusiform cortex';
'R temporal occipital fusiform cortex';
'L inf. temporal gyrus (temporooccipital)';
'R inf. temporal gyrus (temporooccipital)';
'L postcentral gyrus';
'R postcentral gyrus';
'L supramarginal gyrus, post.';
'R supramarginal gyrus, post.';       
'L cingulate gyrus, post.';
'R cingulate gyrus, post.';
'L precentral gyrus';
'R precental gyrus';
'L supramarginal gyrus, ant.';
'R supramarginal gyrus, ant.';
'L parietal operculum cortex';
'R parietal operculum cortex';
'L planum temporale';
'R planum temporale';
'L sup. temporal gyrus, post.';
'R sup. temporal gyrus, post.';
'L middle temporal gyrus, post.';
'R middle temporal gyrus, post.';
'L parahippocampal gyrus, post.';
'R parahippocampal gyrus, post.';
'L temporal frontal cortex, post.';
'R temporal frontal cortex, post.';
'L inf. temporal gyrus, post.';
'R inf. temporal gyrus, post.';
'L insular cortex';
'R insular cortex';
'L heschl''s gyrus';
'R heschl''s gyrus';
'L planum polare';
'R planum polare';
'L central opercular cortex';
'R central opercular cortex';
'L parahippocampal gyrus, ant.';
'R parahippocampal gyrus, ant.';
'L sup. frontal gyrus';
'R sup. frontal gyrus';
'L supplementary motor cortex';
'R supplementary motor cortex';
'L cingulate gyrus, ant.';
'R cingulate gyrus, ant.';
'L sup. temporal gyrus, ant.';
'R sup. temporal gyrus, ant.';
'L middle temporal gyrus, ant.';
'R middle temporal gyrus, ant.';
'L temporal frontal cortex, ant.';
'R temporal frontal cortex, ant.';
'L inf. temporal gyrus, ant.';
'R inf. temporal gyrus, ant.';
'L middle frontal gyrus';
'R middle frontal gyrus';
'L basal forebrain';
'R basal forebrain';
'L paracingulate gyrus';
'R paracingulate gyrus';
'L inf. frontal, pars opercularis';
'R inf. frontal, pars opercularis';
'L frontal operculum cortex';
'R frontal operculum cortex';
'L temporal pole';
'R temporal pole';
'L subcallosal cortex';
'R subcallosal cortex';
'L frontal orbital cortex';
'R frontal orbital cortex';
'L inf. frontal, pars triangularis';
'R inf. frontal, pars triangularis';
'L frontal medial cortex';
'R frontal medial cortex';
'L frontal pole';
'R frontal pole'};            


save m_Labels.mat Labels Names
