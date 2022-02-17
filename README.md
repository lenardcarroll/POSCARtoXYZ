# POSCARtoXYZ
Python script that converts POSCAR and CONTCAR that I use in my project to .xyz files. If your POSCAR or CONTCAR looks generally like this, you can use this script too (an example)

__________
```C Cu```

```   1.00000000000000 ```
    
```     24.6914512445513985    0.0000000000000000    0.0000000000000000```

```     7.4065517955292197   12.8319727856189001    0.0000000000000000```

```     0.0000000001313560    0.0000000000558372   10.0000000000000000```

```   C    Cu```

```   120    10```

```Selective dynamics```

```Direct```

```  0.9999947910080920  0.9996149773863650  0.0000000000000000   F   F   F```

```  0.0000014535230193  0.1662982778370221  0.0000000000000000   F   F   F```

```  0.0999945701665865  0.9996151459185185  0.0000000000000000   F   F   F```

```  ...```

```  ...```

```  ...```
_________

The first line contains some information, the second line the scaling factor or lattice constant, lines 3-5 the cell vectors, line 6 the type of atoms, line 7 the number of atoms for each atom type, lines 8 and 9 more about the coordinates set up and then from line 10 onwards it is coordinates.

If your file is like this, you can use the script as follows:

```
python POSCARtoXYZ.py -inp <INPUTFILENAME> -out <OUTPUTFILENAME>
```
