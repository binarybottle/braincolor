<html>
<head>
<?php include_once("../shared/metatags.php"); ?>
<link rel="stylesheet" type="text/css" href="http://braincolor.org/shared/style.css"> 
 
<script type="text/javascript" src="./scripts/popups.js"></script>

</head>
 <body>

<?php include_once("../shared/banner.php"); ?>

<title>brainCOLORs and optimal colormaps</title>

<div class="main">

<font size="5">Optimal colormaps</font>

<br />
<br />

We compute optimal color assignments for regions, such as those in a 2-D or 3-D brain image.
<br />
The optimization uses a brute force strategy to maximize the distinguishability of adjacent regions 
<br />
while simultaneously choosing perceptually similar colors for groups of regions.
<br />
<br />
We presented a <a href="../docs/SFN2010_BrainCOLORmap_poster_ArnoKlein.pdf">poster</a> at the Society for Neuroscience 2010 conference describing 
<br />
"<b>An interactive tool for constructing optimal brain colormaps</b>"
<div class="xsmalltext">Arno Klein, Andrew Worth, Jason Tourville, Bennett Landman, Tito Dal Canton, Satrajit S. Ghosh, David Shattuck.</div>

<br />

<a href="../docs/SFN2010_BrainCOLORmap_poster_ArnoKlein.pdf"><img src="../docs/SFN2010_BrainCOLORmap_poster_ArnoKlein.jpg" border="1" width="800"></a>

<br />
<br /><br />

<b>Software</b>
<hr>

The software and example input &amp; output are on github, and may also be downloaded from <a href="./code/brainCOLORmap.zip">here</a>.
<br />
<br />

braincolors.py takes in an Excel file with an adjacency matrix, 
where each value signifies adjacency between regions, and outputs the 
optimal assignment of colors to each group of regions on the command line, 
where optimal means maximally distinguishable colors within a neighborhood 
of similar colors in a color space:
 
<br />

<ol>
<li>
Read in an Excel file with a binary (or weighted) adjacency matrix,
   where each row or column represents a region, and each value signifies 
   whether (or the degree to which) a given pair of regions are adjacent.
   Example: (a) column 0 = region abbreviation
            (b) column 1 & row 0 = full region name
            (c) column 2 = group number (each region is assigned to a group)
</li>
<li>
Create a colormap for the number of regions, with hues that are sampled
   from the (approx. perceptually uniform) CIELch cylindrical color space.
</li>
<li>
Convert the matrix from #1 to a graph, where each node represents a region
   and each edge represents the adjacency value between its connected nodes.
</li>
<li>
Break up the graph in #3 into subgraphs, where each subgraph represents
   a group of adjacent regions (assigned the same group number in #1c).
</li>
<li>
Compute every permutation of colors for the nodes of each subgraph in #4,
   with adjacent colors in the color space.
</li>
<li>
Assign each edge in each subgraph the value of the color difference 
   between the colors assigned to its pair of connected nodes in #5.
   (Multiply the connection matrix for each subgraph by
    the color difference matrix for each permutation.)
</li>
<li>
Find the optimal colors for the subgraph nodes that maximizes the sum 
   of the edge values from #6.
</li>
<li>
Plot the colormap, the whole graph, or individual colored subgraphs.
</li>
<li>
Optional: Replace RGB colors in an XML file.  
   The program recolor_eps.[csh,py] takes the output XML to recolor EPS files.<br />
</li>
</ol>

<br />

Also, see <a href="http://perceptvis.cs.sfu.ca//Welcome.html">PerceptVis</a>

<br />
<br />

</div>


<?php include_once("../shared/footer.php"); ?>

</div>
</div>

