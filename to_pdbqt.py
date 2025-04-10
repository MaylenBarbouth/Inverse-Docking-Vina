import os
import subprocess

# Paths
ligands_dir = "../ligandos/"
# ligands_out = "../ligandos_pdbqt/" --> en este caso lo hice manual pero se podria automatizar 

targets_dir = "/home/pps/reverse_docking/50targets"
targets_out = "/home/pps/reverse_docking/reverse_vina/targets_pdbqt/"

pythonsh = "/home/pps/tools/mgltools/bin/pythonsh"
prepare_receptor4 = "/home/pps/tools/mgltools/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py"

# Crear carpetas de salida si no existen
# os.makedirs(ligandos_out, exist_ok=True)
os.makedirs(targets_out, exist_ok=True)

# Recorremos cada subcarpeta de los targets
for nombre_target in os.listdir(targets_dir):
    ruta_subcarpeta = os.path.join(targets_dir, nombre_target)
    
    if os.path.isdir(ruta_subcarpeta):
        # Buscar el archivo .pdb dentro de esta subcarpeta
        for archivo in os.listdir(ruta_subcarpeta):
            if archivo.endswith(".pdb"):
                ruta_pdb = os.path.join(ruta_subcarpeta, archivo)
                nombre_salida = f"{nombre_target}.pdbqt"
                ruta_salida = os.path.join(targets_out, nombre_salida)

                comando = [
                    pythonsh,
                    prepare_receptor4,
                    "-r", ruta_pdb,
                    "-o", ruta_salida,
                ]

                print(f"Convirtiendo {ruta_pdb} → {ruta_salida}")
                subprocess.run(comando)