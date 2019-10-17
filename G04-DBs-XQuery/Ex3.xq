<root>
  {
     let $guid := "15"
     for $c in collection('cursosUA')//curso
     where $c / guid = $guid
     for $d in  $c / departamentos/departamento 		(: for is needed :)
     return 
       <elem>
          { $d / text() }
       </elem>
   }
</root>