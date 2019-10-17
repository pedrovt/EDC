<root>
  {
     let $guid := "15"
     let $c := collection('cursosUA')//curso[guid=$guid]
     return ($c/nome, $c/codigo, $c/grau, $c/local)
   }
</root>