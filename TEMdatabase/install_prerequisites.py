import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def uninstall(package):
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", package, "-y"])

packages = [
    "biopython",
    "elementpath",
    "pandas",
    "db-sqlite3",
    "taxoniq",
    "nglview",
    "tabulate",
    "fuzzywuzzy",
    "pyhmmer",
    "bio",
    "unipressed",
    "uniprot",
    "requests",
    "dict2xml",
    "flatten-json",
    "matplotlib",
    "numpy",
    "hmmer",
    "networkx",
    "sqlite-bro",
    
]

for package in packages:
    install(package)

sdRDM_git = "git+https://github.com/JR-1991/software-driven-rdm.git"
subprocess.check_call([sys.executable, "-m", "pip", "install", sdRDM_git])
