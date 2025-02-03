<?php
if(strpos($_SERVER['HTTP_USER_AGENT'], 'MSIE') !== FALSE)
  echo "You are not worthy! You shall be allowed, only if you come from agent_program";
elseif(strpos($_SERVER['HTTP_USER_AGENT'], 'Trident') !== FALSE) 
      echo "You are not worthy! You shall be allowed, only if you come from agent_program";
elseif(strpos($_SERVER['HTTP_USER_AGENT'], 'Firefox') !== FALSE)
  echo "You are not worthy! You shall be allowed, only if you come from agent_program";
elseif(strpos($_SERVER['HTTP_USER_AGENT'], 'Chrome') !== FALSE)
  echo "You are not worthy! You shall be allowed, only if you come from agent_program";
elseif(strpos($_SERVER['HTTP_USER_AGENT'], 'Opera Mini') !== FALSE)
  echo "You are not worthy! You shall be allowed, only if you come from agent_program";
elseif(strpos($_SERVER['HTTP_USER_AGENT'], 'Opera') !== FALSE)
  echo "You are not worthy! You shall be allowed, only if you come from agent_program";
elseif(strpos($_SERVER['HTTP_USER_AGENT'], 'Safari') !== FALSE)
   echo "You are not worthy! You shall be allowed, only if you come from agent_program";
elseif(strpos($_SERVER['HTTP_USER_AGENT'], 'agent_program') !== FALSE)
   echo "Hello friend, here is your flag: isfcr{w5lc0me_@gent_47}";
 else
	echo "I can't understand!? Find me from agent_program";
?>


<title>He who dwells</title>