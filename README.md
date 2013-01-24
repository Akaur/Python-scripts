Python-scripts
==============

## how to make .dxf files from Python script ##

 You can download Python CAD script from here.
        http://freecode.com/projects/cad-scripts


 Execution of Python scripts

1. Create a file in editor

2. Save the file with .py extension. 

	Ex- Lr.py

3. Open the terminal.

4. Go the directory in which file is stored. 

	Ex- $ cd Downloads/text_to_dxf-1.1/

5. Give the permissions to Lr.py file.
    
       $ chmod ugo+rwx Lr.py

6. Run the Lr.py file and create .txt file that holds coordinates (x,y) for .dxf file.

      $ ./Lr.py > Lr.txt

    You can give any name to file with .txt extension.

7. Now last step is to create .dxf file.

      $ python text_to_dxf.py Lr.txt Lr.dxf.
      
   Lr.dxf file is created in the directory in which you save the Lr.py file. You can open it.
