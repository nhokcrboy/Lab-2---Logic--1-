import os
import glob 
import algorithm

def main():
    # duong dan den thu muc chua script
    script_path = os.path.abspath(__file__)
    folder_path = os.path.dirname(script_path)

    #lay tat ca cac input
    input_files = glob.glob(folder_path + "/INPUT/*")
    
    for i in range(len(input_files)):
        input_files[i] = input_files[i].split("/INPUT/")[1]

    for file in input_files:
        KB,alpha = algorithm.read_input(folder_path + "/INPUT/" + file)
        input_id = file.split("input")[1]
        output_file = "output" + input_id
        temp,out = algorithm.PL_RESOLUTION(KB,alpha)
        algorithm.write_output(folder_path + "/OUTPUT/" + output_file,out,temp)

if __name__ == "__main__":
    main()



