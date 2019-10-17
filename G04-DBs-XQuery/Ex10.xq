<root>
  {
     let $c := collection('cursosUA')//curso
     for $l in distinct-values($c//local)
     order by $l
     return 
       <elem>
          { $l }
       </elem>
   }
</root>
