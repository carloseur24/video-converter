# import ffmpeg
# import re
# # (
# # 	ffmpeg.input("test.webm")
# # 	.output("output.mp4")
# # 	.run()
# # )
# input_file = ffmpeg.input("input.webm")
# output_file = ffmpeg.output(input_file, "output.mp4", vcodec="libx264")

# # Run the command asynchronously and get the progress information
# process = ffmpeg.run_async(output_file, pipe_stdout=True)

# # Define a regular expression to extract the time and speed values
# pattern = re.compile(r"time=(\S+)\s+speed=(\S+)")

# # Loop through the standard output lines
# for line in process.stdout:
#     # Decode the line and strip the newline character
#     line = line.decode("utf-8").strip()
#     # Match the pattern with the line
#     match = pattern.search(line)
#     # If there is a match, print the time and speed values
#     if match:
#         time = match.group(1)
#         speed = match.group(2)
#         print(f"Time: {time}, Speed: {speed}")

import os
import re
import ffmpeg

# Function to convert a webm file to mp4
def convert_webm_to_mp4(input_file, output_file):
    process = ffmpeg.input(input_file).output(output_file, vcodec="libx264").run_async(pipe_stdout=True)
    pattern = re.compile(r"time=(\S+)\s+speed=(\S+)")

    for line in process.stdout:
        line = line.decode("utf-8").strip()
        match = pattern.search(line)
        if match:
            time = match.group(1)
            speed = match.group(2)
            print(f"Time: {time}, Speed: {speed}")

 # Delete the original webm file after successful conversion
    os.remove(input_file)
    print(f"Deleted original file: {input_file}")

# Folder containing webm files
input_folder = "./convert"

# Output folder for mp4 files
output_folder = "./mp4"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Iterate over webm files in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".webm"):
        input_file_path = os.path.join(input_folder, file_name)
        output_file_path = os.path.join(output_folder, file_name.replace(".webm", ".mp4"))
        convert_webm_to_mp4(input_file_path, output_file_path)

print("Conversion completed.")
