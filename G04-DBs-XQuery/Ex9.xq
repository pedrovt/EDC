<root>
  {
     let $c := collection('cursosUA')//curso
     for $a in distinct-values($c//areacientifica)
     order by $a
     return 
       <elem>
          { $a }
       </elem>
   }
</root>
