<root>
  {
     let $guid := "15"
     for $c in collection('cursosUA')//curso 
     where $c / guid = $guid
     return ( $c / guid, $c / home, $c / local)
   }
</root>