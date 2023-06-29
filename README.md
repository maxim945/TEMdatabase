# TEMdatabase
TEM adaptive database for a personal update and discovery of new TEM beta lactamases


Getting started

Create a directory from which you would like to intasll and operate your database,
use this line within your directory to clone the data : git clone https://github.com/PyEED/TEMdatabase.git


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
      and based on the inserted extraction headers. Do not run the populate cell more than once or else copies of the same data will be created.

5.    ClusterTEM1.ipynb is an exampample file to run the complete pipeline.

5.1   Import the data model and create a database.

5.2   Do a BLAST of protein to DNA search and save within an XML document.

5.3   Use the data collected to connected to the external database of genbank, extract all relevant data.

5.4   Populate the database.

6.    numbering_scheme.ipynb, is created to generate a universal numbering of protein or DNA sequences. it generates start and stop positions, and keeps all sequences bounded to have the same length. Alignmrnt of each amino acid to amino acid are numbered, and after the numbering process is done annnotation can be done.

6.1   The numbering scheme process starts by choosing the 5-15 best protein sequences, they should have as much as possible information about them, well studied and agreed upon sequences. those sequences must have relatively high level of identity 60% and above.

6.2   In the next step a Multiple Sequence Alignment(MSA) should be done. in this case ClustalW is used.

6.3   Out of this MSA a profile HMM is created.

6.4   The bounding of the sequences is done by taking a reference sequence and aligning it to the profile HMM. The reference sequence should be a well agreed sequence by the scientific community, this sequence will be aligned to the profile HMM and the numbering from for example 1-263  will be extracted.

6.5   The quesry sequences will be aligned to the profile HMM, each of those sequences will be bounded by the numbering from the reference sequence.

6.6   A numbering scheme will be created, so that all of the sequences are aligned and all of their lengths are exact. 

7.    Within the numbering_scheme.ipynb file there is also a direct connection to the to the network creation in networkx

7.1   in this case the network runs on a matrix which is build based on one point mutation. Any matrix can be applied to this system.

7.2   There is a grid search for the layout algorithm of the networkx. For the spring layout, the algorithm works as followed: there is a "seed" this seed drops all of your data points into space, starting position in space, from that point an "itiration" process runs and using the parameter "K" wich is the attraction force between the datapoints, the data points are restructured. The closer data points will be more denstly clustered and a more distant ones will move further.

7.3   The seeds will run by utilizing the numbering of wanted seed numbers, for eample, from 1-51, you will see 51 graphs, from seed 1-51. take the best seed.

7.4   After the grid search is done and you visually chose the best network, use the best seed to create a network.

8.    The DNAnetwork.ipynb pipeline is very similar to the numbering_scheme.ipynb pipeline, but it runs a pipe line for the DNA sequences.

8.1   It has a feature which detects reverse sequences.It is done by taking arbitrary a sequence, running all sequences based on a pairwise alignment score.

8.2   Taking the lowest score as a reverse sequence.

8.3   It will show a true or false sequence based on the score.

8.4   The True reverse will be switched back into the correct oriantation.


      
