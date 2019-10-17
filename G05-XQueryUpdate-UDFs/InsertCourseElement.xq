  let $bs := collection('cursosUA')//curso 
  for $i in 1 to count($bs)
  return insert node element {'numberToChange'} {"1"} as first into $bs[$i]