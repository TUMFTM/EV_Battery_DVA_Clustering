# EV_Battery_DVA_Clustering
Repository for battery cell clustering based on differential voltage analysis (DVA) in python

This repository provides a codebase for clustering algorithms on interconnected battery cell discharge tests. 

[Manuel Ank](mailto:manuel.ank@tum.de)<br/>
**[Institute of Automotive Technology](https://www.mos.ed.tum.de/en/ftm/home/)**<br/>
**[Technical University of Munich, Germany](https://www.tum.de/en/)**

## Features
- Clustering based on DBSCAN, hierarchical, HDBSCAN and k-means
- Calculating of differential voltage analysis (DVA) and incremental capacity analysis (ICA)
- Peakfinder (extrema)
- Options for plotting, cell discard
- Automated data import from BaSyTec and BioLogic measurement devices

## Usage of the code provided

We are very happy if you choose this code for your projects and provide all updates under GNU LESSER GENERAL PUBLIC LICENSE Version 3 (29 June 2007). Please refer to the license file for any further questions about incorporating these scripts into your projects.
We are looking forward to hearing your feedback and kindly ask you to share bugfixes, improvements and updates on the files provided.

## Getting started

The repository was developed with Python 3.8.

- Setup a virtual environment
- Run 'main.py' with the test file provided in the input folder

If you want to commit an updated version using another software release or a specific toolbox please give us a short heads-up. 

## Detailed guidance

- Enter number of cells and nominal cell capacity in Ah
- Enter path to txt-file; only discharge and rest allowed, discharge pulse optional for resistance determination
- Choose one of the supported measurement equipments; check (and adjust) number of header lines within the corresponding read function
- Check (and adjust) the cluster parameters depending on your cells (type, series production / pre-series, ...)
- Optional: specify cut-off discharge capacity in Ah
- Optional: insert list with cells you want to exclude

## Authors and Maintainers

- Manuel Ank, manuel.ank@tum.de
- Tobias Brehler, tobias.brehler@tum.de

## Contributions

[1] T. Brehler, "Implementation of Clustering Algorithms for Classification of Lithium-Ion Battery Cells for Electric Vehicles", Semester Thesis, Technical University of Munich, 2022

[2] M. Ank, T. Brehler and M. Lienkamp, "Implementation of clustering algorithms for multi-cell characterization of lithium-ion battery cells for electric vehicles", Batterieforum Berlin, 2023.

  
## License

This project is licensed under the GPL License - see the LICENSE file for details.
