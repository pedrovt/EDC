<root>
  {
     let $areaCientifica := "Informática"
     for $c in collection('cursosUA')//curso
     where $c // areacientifica = $areaCientifica (: Not correct to consider areaCientifica :)
     (: where contains($c / areascientificas / areacientifica, $areaCientifica)
     where $c / departamentos = $departamento Does not consider shared courses :)
     
     return 
       <elem>
          { $c }
       </elem>
   }
</root>

