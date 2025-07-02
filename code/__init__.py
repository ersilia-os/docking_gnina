import subprocess
import os


def run_gnina_docking(receptor_path, ligand_path, output_path, config, gnina_path=None):
    """
    Run a GNINA docking process using a defined configuration.

    Parameters:
    -----------
    receptor_path : str
        Path to the receptor file (e.g., 'receptor.pdb').

    ligand_path : str
        Path to the ligand file (e.g., 'ligand.sdf') with molecular conformations.

    output_path : str
        Path to the output file for docking results (e.g., 'docked_output.sdf').

    config : dict
        Configuration dictionary containing:
            Required:
                - 'center_x', 'center_y', 'center_z' : float → docking box center
            Optional:
                - 'size_x', 'size_y', 'size_z' : float → box dimensions (default: 14.0)
                - 'scoring' : str → empirical scoring function (default: 'vinardo')
                - 'cnn_scoring' : str → CNN usage mode (default: 'rescore')
                - 'exhaustiveness' : int → search thoroughness (default: 8)
                - 'minimize' : bool → whether to minimize (default: False)
                - 'seed' : int → random seed for reproducibility (default: 42)
                - 'cpu' : int → the number of CPUs to use (default: 1)
                - 'num_modes' : int → maximum number of binding modes to generate (default: 9)

    gnina_path : str, optional
        Path to the GNINA executable. Defaults to '../gnina/gnina1.3.1' relative to script location.
    """
    if gnina_path is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        gnina_path = os.path.abspath(os.path.join(script_dir, "..", "gnina", "gnina1.3.1"))

    # Required box parameters
    center_x = config["center_x"]
    center_y = config["center_y"]
    center_z = config["center_z"]

    # Optional settings
    size_x = config.get("size_x", 14.0)
    size_y = config.get("size_y", 14.0)
    size_z = config.get("size_z", 14.0)
    scoring = config.get("scoring", "vinardo")
    cnn_scoring = config.get("cnn_scoring", "rescore")
    exhaustiveness = config.get("exhaustiveness", 8)
    minimize = config.get("minimize", False)
    seed = config.get("seed", 42)
    cpu = config.get("cpu", 1)
    num_modes = config.get("num_modes", 1)

    # Build command
    cmd = [
        gnina_path,
        "-r", receptor_path,
        "-l", ligand_path,
        "--center_x", str(center_x),
        "--center_y", str(center_y),
        "--center_z", str(center_z),
        "--size_x", str(size_x),
        "--size_y", str(size_y),
        "--size_z", str(size_z),
        "--scoring", scoring,
        "--cnn_scoring", cnn_scoring,
        "--exhaustiveness", str(exhaustiveness),
        "--seed", str(seed),
        "--cpu", str(cpu),
        "--num_modes", str(num_modes),
        "-o", output_path
    ]

    if minimize:
        cmd.append("--minimize")

    subprocess.run(cmd)

