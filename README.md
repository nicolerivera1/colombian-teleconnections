# Colombian Teleconnections

![UdeA Logo](https://www.udea.edu.co/wps/wcm/connect/udea/2288a382-341c-41ee-9633-702a83d5ad2b/logosimbolo-horizontal-png.png?MOD=AJPERES&CVID=ljeSAX9)

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/nicolerivera1/colombian-teleconnections)](https://github.com/nicolerivera1/colombian-teleconnections/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/nicolerivera1/colombian-teleconnections)](https://github.com/nicolerivera1/colombian-teleconnections/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/nicolerivera1/colombian-teleconnections)](https://github.com/nicolerivera1/colombian-teleconnections/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/nicolerivera1/colombian-teleconnections)](https://github.com/nicolerivera1/colombian-teleconnections/pulls)


## Table of Contents

1. [Introduction](#introduction)
2. [Usage](#usage)
3. [Citation](#citation)
4. [Contributing](#contributing)
5. [Acknowledgments](#acknowledgments)

## Introduction 

Welcome! This repository contains the code used in the Master's thesis titled "Colombian climate teleconnections from complex networks and information transference" by Nicole Rivera at the University of Antioquia.

The research aims to build a complex climate network to understand how the Pacific and Atlantic Oceans influence Colombian climate.

We use complex network analysis, a new approach in climate science, to explore teleconnections (atmospheric linkages) and their impact on Colombia's climate.

The code allows us to analyze these teleconnections and their cascading effects, helping us understand how distant climate events can influence Colombian temperature and precipitation.

You can reproduce our results or make your analysis using these codes and build the appropriate folder structure to run the scripts.


## Usage

To start using the Colombian teleconnections code, follow these recommendations:

1. Clone the repository.

   ```bash
   git clone https://github.com/nicolerivera1/colombian-teleconnections.git
   ```

2. Download and format the data you will use using the codes at inf-transference/get_climate_data. We recommend you have a CS3 account to download the ERA5 datasets by running

    ```bash
    python cds_request.py
    ```

for each variable of interest. Then download the NOAA indexes time series run the notebook `get_indexes_timeseries.ipynb` and give it spatial structure by running

   ```bash
   bash enlarge_nc_indexes.sh
   ```

and specify the source folder where you downloaded your NOAA time-series and the destination folder where you will save the resulting nc files.

If you wish to cut the specific study area of our study run the bash file `select_colombia_grid.sh` for all your nc files. 

3. Calculate the normalized information transference between your data. Organize your indexes and variables in separate folders and then loop over them by running

    ```bash
    bash loop_inf_transf_calculation.sh
    ```

4. Build your adjacency matrices. Once you have the information transference files, run

    ```bash
    python build_adjacency_matrix.py
    ```

specifying your threshold and paths. 

5. Calculate the network properties by running the example codes in the network_analysis folder. 


## Citation

According to the MIT license, if you use any part of this code, please cite it as:

Rivera-Parra, N. (2024). Colombian teleconnections repository [Source code]. GitHub Repository. https://github.com/nicolerivera1/colombian-teleconnections


## Contributing

We welcome contributions to this project! Here's how you can get involved:

1. **Fork the Repository:**  
   Click the "Fork" button on the main repository page. This creates a copy of the code in your own GitHub account.

2. **Create a Branch:**
   Make your changes on a new branch in your forked repository. This keeps your changes separate from the main codebase.

3. **Commit Your Changes:**
   Once you're happy with your changes, commit them to your branch with a clear and descriptive commit message.

4. **Create a Pull Request:**
   Push your changes to your forked repository and open a Pull Request (PR) from your branch to the main branch of the original repository. This sends a notification to the maintainers about your proposed changes.

5. **Get Feedback:**
   We will review your Pull Request and provide feedback. Be sure to address any comments or questions before merging.

**Contact:**

If you have any questions about contributing, feel free to open an Issue in the repository or send an email to nicole.rivera@udea.edu.co


## Acknowledgments

This project would not have been possible without the invaluable support of:

* My professors and thesis advisors, Isabel Hoyos and Boris Rodriguez, for their guidance and mentorship throughout this research.
* The University of Antioquia for providing the academic environment and resources necessary for this work.
* My loved ones, for their unwavering support and encouragement throughout this journey.
