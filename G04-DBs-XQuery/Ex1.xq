
<root>
  {
    for $c in collection('cursosUA')//curso 
    return
      <elem>
        { $c / guid }
        { $c / nome }
      </elem>
  }
</root>
