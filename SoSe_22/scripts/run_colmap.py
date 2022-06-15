import os
import sys
import getopt
import subprocess

def execute_script(script, images):
	os.chdir(images)
	# colmap2nerf expects a "y/n" -> just pipe a y lol
	command = f'echo y | python {script} --run_colmap --aabb_scale 16'
	p = subprocess.Popen(
		[command],
		shell=True,
		stdin=None,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		close_fds=True)
	out = p.communicate()[0]
	print(out)


def main():
	argv = sys.argv[1:]
	PATH_TO_SCRIPT=""

	try:
		opts, args = getopt.getopt(argv, "hs:i:")
	except:
		print("Error")

	# help usage info
	for opt, args in opts:
		if opt in ["-h"]:
			print(f'Usage {sys.argv[0]} -s <path to colmap2nerf.py> [path to /images]') 
			exit() 

	for opt, args in opts:
		if opt in ["-s"]:
			PATH_TO_SCRIPT = args
	
	# loop throuh images
	image_paths = argv[2:]
	for imp in image_paths:
		print(imp)
		execute_script(PATH_TO_SCRIPT, imp)

if __name__=='__main__':
	main()



