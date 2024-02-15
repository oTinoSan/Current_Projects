# IMMEDIATE
- TensorRT libraries installed
- Test it (will need to make some sort of dummy script or something)
- Check the version number and cross-reference its compability with PyTorch (which versions are supported)

# NEAR TERM
create a clean directory for benchmarking (do not alter current directoy -- do the following steps in a new directory so that we can cont. work until complete)
- dataset directory (+2: mars and fire)
- trained model directory to include subdirectories (+2: mars and fire, non-quantized, quantized, etc...)
- results directory (plots/charts and terminal output should save here, each folder titled 'mars' or 'fire' plus '[date+time]' of test.)
- main.py (this is the benchmarking script) to take command-line arguments 'mars' or 'fire' and 'model path' to point to the correct dataset and model
- rename virtual environment to 'benchmark'

# MEDIUM TERM 
develop a new benchmark script that directly accesses jtop to calculate and plot benchmarks so that we no longer need to run jtop logger in the background and manually create charts using excel
--- measure and plot overall CPU usage (average across all cores) for duration of script execution
--- measure and plot overall GPU usage (average across all cores) for duration of script execution
--- measure and plot shared-RAM usage for duration of script execution
--- measure and plot total power usage for duration of script execution
--- the benchmark script already measures average inference time, preprocessing, and IO 



check tensor rt and see version, compatibility and if it works on turtlebot (30 or 40) (and 35)
what does it mean to quatize a model

jetson-stats, should see if tensorrt was installed

v_env mso resnet 50 - not in benchmarking directory
