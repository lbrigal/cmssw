# some example testing workflows for unscheduled mode - should eventually be deleted and made the default...
# import the definition of the steps and input files:
from  Configuration.PyReleaseValidation.relval_steps import *

# here only define the workflows as a combination of the steps defined above:
workflows = Matrix()

# each workflow defines a name and a list of steps to be done. 
# if no explicit name/label given for the workflow (first arg),
# the name of step1 will be used

# 50 ns at 8 TeV
workflows[10025] = ['', ['TTbar','DIGI','RECOUNSCH','HARVEST','ALCATT']]
workflows[11325] = ['', ['TTbar_13','DIGIUP15','RECOUP15UNSCH','HARVESTUP15','ALCATT']]
