[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6453048.svg)](https://doi.org/10.5281/zenodo.6453048)

# Affine Parametric Neural Networks

Second hands-on on **Parametric Neural Networks** (pNNs).

> [!NOTE]  
> This hands-on is taken from the ML-INFN Knowledge base, more info [here](https://confluence.infn.it/spaces/MLINFN/pages/109151730/14.+Signal-background+classification+with+Parametric+Neural+Networks) (credits L.Anzalone, T.Diotalevi)

pNNs are a kind of neural networks, developed by [Baldi et al.](https://arxiv.org/pdf/1601.07913), which are mainly used for *signal-background classification* in High-Energy Physics (HEP). In our recent [paper](https://iopscience.iop.org/article/10.1088/2632-2153/ac917c), we propose various improvements to the original pNN, 
such as: 
* The *affine architecture*: based on interleaving multiple **affine-conditioning layers**;
* Guidelines on how to assign the *physics parameter* (e.g. the particle mass);
* The *balanced training* procedure, in which we build balanced mini-batches by leveraging the structure of both the 
signal and background.

This branch of the repo is about a **complete tutorial** on how to define, and apply pNNs: everything is described in 
the `Affine_Parametric_NN.ipynb` notebook.

## How to run this hands-on (standalone)

During the hands-on session, we will use a cloud facility (from the [ICSC Spoke2 project](https://www.supercomputing-icsc.it/en/spoke-2-fundamental-research-space-economy-en/)). However, if you want to run the code in your personal machine, I prepared a Docker container with all the dependencies installed.

The instructions on how to run the container are available in this [Github repository](https://github.com/tommasodiotalevi/jupyter-lab_root): 

> [!IMPORTANT]
> This repository must be cloned inside the `persistent-storage` folder of the other repository, in order to see it inside the container.

## Alternative installation
In the [original repository](https://github.com/Luca96/affine-parametric-networks/tree/tutorial) you will find additional installation modes (both local and using Docker).


---
---
## How to Cite

If you use the code and/or the dataset we provide for your own project or research, please cite our paper:

```latex
@article{Anzalone_2022,
   doi = {10.1088/2632-2153/ac917c},
   url = {https://doi.org/10.1088/2632-2153/ac917c},
   year = 2022,
   month = {sep},
   publisher = {{IOP} Publishing},
   volume = {3},
   number = {3},
   pages = {035017},
   author = {Luca Anzalone and Tommaso Diotalevi and Daniele Bonacorsi},
   title = {Improving parametric neural networks for high-energy physics (and beyond)},
   journal = {Machine Learning: Science and Technology}
}
```

Dataset citation:

```
@dataset{hepmass_imb,
  author={Luca Anzalone and Tommaso Diotalevi and Daniele Bonacorsi},
  title={HEPMASS-IMB},
  month=apr,
  year=2022,
  publisher={Zenodo},
  doi={10.5281/zenodo.6453048},
  url={https://doi.org/10.5281/zenodo.6453048}
}
```

