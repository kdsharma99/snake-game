import cx_Freeze
executables=[cx_Freeze.Executable("snakegame.py")]
cx_Freeze.setup(name="Snake Game by Kushal Sharma",
options={"build_exe":{"packages":["pygame"],
"include_files":["bg.mp3","game_over.jpg",
"Highscore.txt","home.jpg","gameover.mp3"]}},
executables=executables
)