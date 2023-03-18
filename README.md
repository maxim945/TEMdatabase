# TEMdatabase
TEM adaptive database for a personal update and discovery of new TEM beta lactamases


Getting started

1. First you have to install all dependencies.
    
1.1. Go into the TEMdatabase directory on your linux terminal.

1.2. Run the installaion line from within the TEMdatabase directory: python3 install_prerequisites.py 

1.3. Alternatively you can go to Install_Packages directory, open the Install.ipynb file and run it from jupyter notebook.

After the installation is done.

2. Collect the data with which you will populate your database.
  
2.1. Open the BLAST.ipynb file.

2.2. You will need a seed fasta file to start from doing your BLAST search.(as an example TEM-1 beta lactamse).

2.3. The serach parameters can be changed based on the inserted parameters. For further help:
      https://biopython.org/docs/1.75/api/Bio.Blast.NCBIWWW.html
      
2.4. The result is being saved as an XML file inside the Document directory.

3. Data Model creation.
    
3.1. There are 2 option to create the data model.

3.1.1 The first option is to take the PyEED template from our PyEED Github webpage (https://github.com/PyEED) change the template file as instructed on the PyEED README and create your own repository.

3.1.2 You can create your data model locally, just add the required changes to the markdown document and run it locally. The local file is located in Documents/DataModel/TEMdatamodelProtein.md.

After the datamodel was created.

4.    Open the jupyter notebook file TEMdatabase.ipynb, run this script.
    
4.1   This script will import the needed sdRDM modules and import the data model. There are 2 options as previously described, you can use the from_git function to extract the datamodel from the online repository or use the from_markdown for the locally created data model.
      
4.2   The data model will be converted to a database, this will be an empty database.

4.3   Lastly the database will be populated based on on the information that you have on your XML document
      and based on the inserted extraction headers. Do not run the populate cell more then once or else copies of the same data will be created.
      
