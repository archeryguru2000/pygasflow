## pygasflow

pygasflow provides a few handful functions to quickly perform quasi-1D ideal gasdynamic computations with Python (see requirements below).

At the moment, the following flow relations are implemented:
* Isentropic flow
* Fanno flow
* Rayleigh flow
* Shock wave relations (normal shock, oblique shock, conical shock)

Look at the [Usage](#Usage) section for more informations.

**This repository is still a Work In Progress and need to be properly tested. Use it at your own risk.** If you find any errors, submit an issue or a pull request!

## Requirements and Installation

* Python >= 3.6
* numpy
* scipy
* matplotlib

To install this package:
1. Download this repository.
2. Open the terminal, move into the `pygasflow` parent folder.
3. Install it with this command (all the dependencies should auto install): `python3 -m pip install .`


## Usage

The easiest way to use this code is to call the interested solver. At the moment, the following solvers are implemented:

* `Isentropic_Solver`
* `Fanno_Solver`
* `Rayleigh_Solver`
* `Shockwave_Solver`
* `Conical_Shockwave_Solver`

All the solver are located into the `solvers` sub-package. For example, if you need to use the `Isentropic_Solver`, just import it like this: 

`from pygasflow.solvers import Isentropic_Solver`

The [examples](examples/) folder provide a few usage examples. I strongly suggest to take a look at them.

Should the solver not be sufficient for your use case, feel free to explore the code implemented inside each flow's type, maybe you'll find a function that suits you. The code is well documented: I went for a natural language nomenclature since (I bet) most of us are using and advanced editor with autocompletion. For instance, the critical temperature T/T* is defined as Critical_Temperature_Ratio across the different flows, and so on. To import a function defined inside a specific flow, you can do (for instance):

`from pygasflow.isentropic import Critical_Temperature_Ratio`