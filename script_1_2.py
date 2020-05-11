import subprocess
import sys


EXECUTE_ENDED_STR = "Execution ended after 0:00:05"
PIPELINE_PREROLLING = "Pipeline is PREROLLING"
#PIPELINE_PLAYING = "Setting pipeline to PLAYING"
PIPELINE_PREROLLING_FAIL = "ERROR: pipeline doesn't want to preroll."
AUDIO_STREAM_FFMPEG_CHECK = "Stream #0:1(eng): Audio:"

def get_answer():
    with open("./student_response.txt") as file:
        return file.read()

STUD_CODE = get_answer()
list_of_used_by_student_elements = STUD_CODE.split()
video_file_name = list_of_used_by_student_elements[-1].partition("=")[2]

GRADE = 3

result = subprocess.run(['bash','-O','extglob', '-c', STUD_CODE], stdout=subprocess.PIPE)
resDecodedStdOut = result.stdout.decode('utf-8')

check = subprocess.run(['ffmpeg','-i', video_file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
checkDecodedStdOut = check.stderr.decode('utf-8')

if (EXECUTE_ENDED_STR in resDecodedStdOut):
        GRADE = 3
        #GRADE IS STILL MAX
        if not (AUDIO_STREAM_FFMPEG_CHECK in checkDecodedStdOut):
                GRADE = 2
else:
        if (PIPELINE_PREROLLING in resDecodedStdOut and PIPELINE_PREROLLING_FAIL in resDecodedStdOut):
                GRADE = 1
        else:
                GRADE = 0



sys.stdout.write(str(GRADE))
sys.stdout.flush()
sys.exit(GRADE)

