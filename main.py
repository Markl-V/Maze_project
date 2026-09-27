def main(path_to_generate, path_to_labir, path_to_solutions):

    from EFTA_solver.py import maze_list
    from EFTA_solver.py import path
    from EFTA_solver.py import list_maze_path
    from generator.py import gener

    gener(path_to_generate)
    arr, s, f, h, w = maze_list(path_to_labir)
    p = path(arr, s, f)
    list_maze_path(arr, h, w, s ,f, p, path_to_solutions)