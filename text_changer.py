import os
import re

script_dir = os.path.dirname(__file__)
rel_path_fin = 'finland.txt'
rel_path_phi = 'philosophy.txt'
rel_path_lin = 'linguistics.txt'
rel_path_fin_changed = 'finland-changed.txt'
rel_path_phi_changed = 'philosophy-changed.txt'
rel_path_lin_changed = 'linguistics-changed.txt'
abs_path_fin = os.path.join(script_dir,rel_path_fin)
abs_path_phi = os.path.join(script_dir,rel_path_phi)
abs_path_lin = os.path.join(script_dir,rel_path_lin)
abs_path_fin_changed = os.path.join(script_dir,rel_path_fin_changed)
abs_path_phi_changed = os.path.join(script_dir,rel_path_phi_changed)
abs_path_lin_changed = os.path.join(script_dir,rel_path_lin_changed)

with open(abs_path_fin,'r') as f:
    f = f.read()
    q = (re.sub(r'Финляндия\s+', 'Малайзия', f))
    with open(abs_path_fin_changed,'w') as fc:
        fc.write(q)

with open(abs_path_phi,'r') as p:
    p = p.read()
    q = (re.sub(r'философия\s+', 'астрология', f))
    with open(abs_path_phi_changed, 'w') as fc:
        fc.write(q)

with open(abs_path_lin,'r') as f:
    f = f.read()
    q = (re.sub(r'язык\s+', 'шашлык', f))
    with open(abs_path_lin_changed,'w') as fc:
        fc.write(q)