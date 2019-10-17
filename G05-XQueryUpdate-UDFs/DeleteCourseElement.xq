  let $bs := collection('cursosUA')//curso 
  for $i in $bs/numberToChange
  return delete node $i