  let $bs := collection('cursosUA')//curso 
  for $y in $bs/numberToChange
  return replace node $y/text() with 'POTATOESS'