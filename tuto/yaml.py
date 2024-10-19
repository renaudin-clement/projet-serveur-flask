import yaml , os.path
data = yaml.safe_load(
open(
    os.path.join(
    os.path. dirname ( __file__ ),"data.yml")))