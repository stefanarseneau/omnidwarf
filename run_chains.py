import pandas as pd
import pyvo
import os

def downloadNGF():
    tap_service = pyvo.dal.TAPService("http://TAPVizieR.u-strasbg.fr/TAPVizieR/tap/")
    QUERY = """select GaiaEDR3, RA_ICRS, DE_ICRS, Plx - ZPCor as PlxZPCorr, e_Plx, meanAV 
            from \"J/MNRAS/508/3877/maincat\" """
    data = tap_service.search(QUERY).table.to_pandas()
    data.to_parquet("GaiaDR3_white_dwarfs.pqt")
    return data

if __name__ == "__main__":
    try:
        data = pd.read_parquet("GaiaDR3_white_dwarfs.pqt")
    except FileNotFoundError:
        print("File 'GaiaDR3_white_dwarfs.pqt' not found, downloading!")
        data = downloadNGF()

    os.system("ember submit fit-sed /project/mesaelm/omnidwarf/GaiaDR3_white_dwarfs.pqt /project/mesaelm/omnidwarf/chains/ --xpphoto --synthetic --mcmc --source-id GaiaEDR3 --ra RA_ICRS --dec DE_ICRS --parallax PlxZPCorr --parallax-error e_Plx --meanav meanAV --numtasks 512")
