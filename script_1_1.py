import subprocess
import sys

ARGS_THAT_DECREMENTS_GRADE = ['playbin', 'uridecodebin', 'decodebin', 'autoaudiosink']

EXECUTE_ENDED_STR = "Execution ended after 0:04:"
PIPELINE_PREROLLING = "Pipeline is PREROLLING"
#PIPELINE_PLAYING = "Setting pipeline to PLAYING"
PIPELINE_PREROLLING_FAIL = "ERROR: pipeline doesn't want to preroll."

def get_answer():
    """
    Read student answer from the file.
    :return: Student answer.
    """
    with open("./student_response.txt") as file:
        return file.read()

STUD_CODE = get_answer()

GRADE = 3
#FINAL_CONCLUSION = ""
#ERROR_STUDENT_USED_BAD_ELEMENTS = "Был использован один элементов: 'playbin', 'uridecodebin', 'decodebin', 'autoaudiosink'"
#ERROR_AUDIO_NOT_PLAYED = "mp3 файл не воспроизводится"

result = subprocess.run(['bash','-O','extglob', '-c', STUD_CODE], stdout=subprocess.PIPE)
resDecodedStdOut = result.stdout.decode('utf-8')

#print(resDecodedStdOut)

if (EXECUTE_ENDED_STR in resDecodedStdOut):
	#print("Audio played successfully")

	list_of_used_by_student_elements = STUD_CODE.split()

	student_used_element_that_decrements_grade = any(item in list_of_used_by_student_elements for item in ARGS_THAT_DECREMENTS_GRADE)

	if (student_used_element_that_decrements_grade):
		GRADE = 2
		#FINAL_CONCLUSION =  ERROR_STUDENT_USED_FUCKY_ELEMENTS
	#else:
		#FINAL_CONCLUSION = "All is ok"

else:
	#print("Audio not played")
	#FINAL_CONCLUSION = ERROR_AUDIO_NOT_PLAYED
	if (PIPELINE_PREROLLING in resDecodedStdOut and PIPELINE_PREROLLING_FAIL in resDecodedStdOut):
		GRADE = 1
	else:
		GRADE = 0



sys.stdout.write(str(GRADE))
sys.stdout.flush()
sys.exit(GRADE)

