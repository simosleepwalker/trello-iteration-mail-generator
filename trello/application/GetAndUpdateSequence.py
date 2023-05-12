import os


class GetAndUpdateSequence:

    def __init__(self):
        r_seq = None
        if os.path.isfile("./iteration_seq.seq"):
            with open("./iteration_seq.seq", "r") as r_file:
                r_seq = r_file.read()
        self.seq = 1 if r_seq is None or r_seq == '' else r_seq

    def get_and_update(self):
        w_file = open("./iteration_seq.seq", "w")
        w_file.write(str(int(self.seq) + 1) + '\n')
        w_file.close()
        return self.seq
