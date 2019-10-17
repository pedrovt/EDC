<root>
  {
     let $departamento := "Departamento de Eletrónica, Telecomunicações e Informática"
     for $c in collection('cursosUA')//curso
     (: where contains($c / departamentos, $departamento) Not correct. Searching in the text inside the element:)
     where $c // departamento = $departamento (: Not correct to consider departamentos :)
     
     return 
       <elem>
          { $c/nome }
       </elem>
   }
</root>

