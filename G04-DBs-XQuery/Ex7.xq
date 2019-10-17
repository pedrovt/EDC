<root>
  {
     let $local := "ESTGA, Águeda"
     for $c in collection('cursosUA')//curso
     where $c // local = $local 
     
     return 
       <elem>
          { $c /nome }
       </elem>
   }
</root>

