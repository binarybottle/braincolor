<html>
<head>
<?php include_once("../shared/metatags.php"); ?>
<link rel="stylesheet" type="text/css" href="http://braincolor.org/shared/style.css"> 
 
<script type="text/javascript" src="../scripts/popups.js"></script>

</head>
 <body>

<?php include_once("../shared/banner.php"); ?>

<title>brainCOLOR: Collaborative Open Labeling Online Resource</title>

<?php
 $survey_width = 600;
 $survey_height = 1500;
 $survey_height2 = 600;
?>

<title>brainCOLOR: Collaborative Open Labeling Online Resource</title>
<div class="main_wide">

<font size="5">Cortical labeling <b>survey</b></font>

<br />

<table>
 <tr>
  <td valign="top">
   <br />

Please fill in your name, email address, and the survey, then click the Submit button at the bottom of the survey. Please refer to the figures and tables,
and click on them to enlarge.

<br /><br />

<iframe src="https://spreadsheets.google.com/embeddedform?key=t4YKiN9UwlpXbRXGKgOYn7g" width="<?php echo $survey_width; ?>" height="<?php echo $survey_height; ?>" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>

<td width="40"></td>

<td valign="top">

<a href="images/Figure2_SulciRegions_Tourville2009.png" onClick="return popup640(this,'figure 2: sulci_regions')"><img src="images/Figure2_SulciRegions_Tourville2009.png" width=360 border="0"></img></a>

<a href="images/Figure3_SulciRegions_Tourville2009.png" onClick="return popup640x480(this,'figure 3: sulci_regions2')"><img src="images/Figure3_SulciRegions_Tourville2009.png" width=360 border="0"></img></a>

   <table>
    <tr>
     <table>
      <tr>
       <td valign="top">
<a href="images/Table2_Regions_Tourville2009.png" onClick="return popup400(this,'table2: regions')"><img src="images/Table2_Regions_Tourville2009.png" width="240" border="0"></img></a>
       </td>
       <td valign="top">
<a href="images/Table1_Sulci_Tourville2009.png" onClick="return popup400(this,'table1: sulci')"><img src="images/Table1_Sulci_Tourville2009.png" width=290 border="0"></img></a>
       </td>
      </tr>
     </table>
     <table>
      <tr>
       <td valign="top">
<a href="images/Table3_Planes_Tourville2009.png" onClick="return popup640x480(this,'table3: planes')"><img src="images/Table3_Planes_Tourville2009.png" width="530" border="0"></img></a>
       </td>
      </tr>
     </table>
    </tr>
   </table>  
     
  </td>
 </tr>
</table>

<br />

<!--?php include_once("../shared/license.php"); ?-->
<?php include_once("../shared/footer.php"); ?>

</div>

