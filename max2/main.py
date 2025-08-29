# Aug-24-2025
# main.py

from pathlib import Path
import time

from max2.src import cfg
from max2.src.utils import init_directory, remove_directory
from max2.src.get_shapes_distance import get_shapes_distance


# Input Data
# -------------------------------------------------------------
cfg.image_name = 'loc_left.png'
cfg.templ_name = 'loc_right.png'
# -------------------------------------------------------------

print(f'\nWait...')

cfg.dir_data = 'IMAGES_DATA'
cfg.dir_debug = '_RESULTS_max2'

cfg.path_image \
    = str(Path.cwd() / cfg.dir_data / cfg.image_name)
cfg.path_templ \
    = str(Path.cwd() / cfg.dir_data / cfg.templ_name)

if cfg.debug_mode:
    init_directory(cfg.dir_debug)
else:
    remove_directory(cfg.dir_debug)

begin = time.time()

distance = get_shapes_distance(cfg.path_image, cfg.path_templ)

end = time.time()

print(f'\n{cfg.image_name}  &  {cfg.templ_name}'
      f'\ndistance = {distance:.5f}'
      f'\ntime = {(end - begin):.1f} sec')
