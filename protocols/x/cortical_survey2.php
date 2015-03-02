<?php include_once("../shared/header_start.php"); ?>

</head>
 <body>

<?php include_once("../shared/banner.php"); ?>

<title>brainCOLOR: Collaborative Open Labeling Online Resource</title>

<?php
 $survey_width = 600;
 $survey_height = 900;
 $survey_height2 = 600;
?>

<title>brainCOLOR: Collaborative Open Labeling Online Resource</title>
<div class="main">

<b>
<font size="5">Proposed Cortical Parcellation Protocol: 
&nbsp;&nbsp;
<a href="cortical_survey.php">SURVEY 1</a>
&nbsp;&nbsp;
SURVEY 2
</font>
</b>

<br /><br />

<table>
 <tr>
  <td width="725">
SURVEY 2 gives you the opportunity to state your preference for additional data you would care to have us manually label with the proposed labeling protocol.
Please fill in your name and email address, fill in the survey, and click the Submit button at the bottom of the survey.
  </td>
 </tr>
</table>
<br />
<br />

<iframe src="https://spreadsheets.google.com/embeddedform?key=t_doFFSg1xbVkYd43R2pn6Q" width="<?php echo $survey_width; ?>" height="<?php echo $survey_height2 ?>" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>

<br />
<!--?php include_once("../shared/license.php"); ?-->
<?php include_once("../shared/footer.php"); ?>

</div>

