Spaun 1.0
=========

Spaun is a biologically realistic model of cognition that is not only
able to perform multiple (at least 10) cognitive, perceptual, and
motor tasks, but also utilizes the same model parameters across all
tasks. Spaun is able to perform tasks that encompass strictly visual
tasks (e.g. recognition of handwritten digits), memory tasks
(e.g. forward and backward recall of a list), simple cognitive tasks
(e.g. counting), and complex fluid intelligence tasks (e.g. solving
the Raven's Progressive Matrices).

* [Spaun videos](https://xchoo.github.io/spaun2.0/videos.html)
* [Brief description of Spaun's architecture](https://www.nengo.ai/build-a-brain/)

## Instructions

To run Spaun, follow these instructions:

1. Install Nengo 1403 as per the INSTALL-NENGO.txt file.
2. Run Nengo 1403.
3. Within Nengo, press CTRL+P to bring up the scripting console, and
   type `run run_spaun_win.py` (if you are on a Windows-based system)
   or `run run_spaun_lin.py` (if you are on a Linux/Unix-based
   system).
4. The log files that are generated can be found in `spaun/out_data`
   located within this directory.

## Notes

* This model requires a machine with at least 24GB of RAM to run.
  Estimated run times for a quad-core 2.5GHz are 3 hours per 1 second
  of simulation time.
* See the `run_spaun.py` file in the spaun directory for experiment
  options.
* Model parameters can be altered in the `conf.py` file found in the
  spaun directory.
* To load the model with a different number of dimensions than the
  default (default = 512 dimensions), alter the line `num_dim = 512`
  in the `conf.py` file. Setting the number to 4 enables the model to
  be loaded on a 2GB machine.
