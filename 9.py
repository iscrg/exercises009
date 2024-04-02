class StrandsDNA:
    def __init__(self):
        self.all_strands = []

    def add_strands(self, strands: str):
        """
        Adds DNA strands that are written in the string strands separated by a space.
        :param strands: A string containing DNA strands separated by spaces.
        :return: None
        """
        self.all_strands.extend(strands.split())

    def get_max_strands(self):
        """
        :return: A string containing chains of maximum length,
                 separated by a space, without repetition, in alphabetical order.
        """
        max_length = max(len(strand) for strand in self.all_strands)
        max_strands = sorted(set(strand for strand in self.all_strands if len(strand) == max_length))
        return ' '.join(max_strands)


dna = StrandsDNA()
dna.add_strands('hufduhifd fsduhisafduhisdfauohiasfd fh ufsduihasfduhoifauhio fsdhu sfiouhasfdhui fdshuasfuioasfdhouifasd fdhasifhasduifhasdoui')
dna.add_strands('fdsjisadjifsdapo jfasdpafsdjifjfsdj kdsafplfadpfasdj ewf jkfwekj felqwfdj sfadj dfsaj fsadklasfdkjadsfkl')
print(dna.get_max_strands())
